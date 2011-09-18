from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from mixmarket.items import MixmarketItem


class MixMarketSpider(BaseSpider):
    name = "mixmarket"
    allowed_domains = ["mixmarket.org"]
    start_urls = [
        "http://mixmarket.org/mfi/country/Afghanistan",
    ]

    def extract_sum(self, piece):
        """ views-field-sum parsing
        These have a numeric part, an order part, and a meta part
        """
        # Numeric part, e.g "3.1".  We also need to strip the commas ","
        # out of the number before converting it to a float.
        tmp = piece.select('span/span[@class="numeric"]/text()').extract()[0]
        num = float(tmp.replace(",", ""))

        # Order part, e.g. "thousand" or "million"
        tmp = piece.select('span/span/span[@class="order"]/text()').extract()
        if tmp != []:
            if tmp[0] == u'thousand':
                num = num * 1000.0
            if tmp[0] == u'million':
                num = num * 1000000.0
        meta = piece.select('label/span[@class="meta"]/text()').extract()[0]
        return num, meta

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # Extract company detail URLs from country overview pages
        company_detail_urls = hxs.select('//td[@class="views-field views-field-name active"]/a/@href').extract()
        for url in company_detail_urls:
            print "Spidering", 'http://mixmarket.org' + url
            yield Request('http://mixmarket.org' + url, callback=self.company_parse)

    def company_parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = MixmarketItem()

        # The institution name and country are in the page title, have to
        # do a little cleaning up and split on "|".
        co_name = hxs.select('//title').extract()[0]
        co_name = co_name.replace("<title>", "").replace("</title>", "").replace("MFIs in ", "")
        co_name = co_name.split("|")
        item['co_name'] = co_name[0]
        item['country'] = co_name[1]

        co_date_inc = hxs.select('//div[@class="field field-type-date field-field-mfi-date"]/div/div/span/text()').extract()
        item['co_date_inc'] = co_date_inc[0]

        co_rating = []
        for diamonds in range(5):
            co_rating = hxs.select("//span[@class=\"diamonds diamonds-%d\"]/text()" % diamonds).extract()
            if co_rating != []:
                item['co_rating'] = int(co_rating[0])
                break

        # Portfolio (loans)
        co_portfolio, co_portfolio_meta = self.extract_sum(hxs.select('//div[@class="views-field-sum"]'))
        item['co_portfolio'] = co_portfolio
        item['co_portfolio_meta'] = co_portfolio_meta

        # Assets
        co_assets, co_assets_meta = self.extract_sum(hxs.select('//div[@class="views-field-sum-3"]'))
        item['co_assets'] = co_assets
        item['co_assets_meta'] = co_assets_meta

        # Deposits
        co_deposits, co_deposits_meta = self.extract_sum(hxs.select('//div[@class="views-field-sum-2"]'))
        item['co_deposits'] = co_deposits
        item['co_deposits_meta'] = co_deposits_meta

        # Number of active borrowers
        co_borrowers, co_borrowers_meta = self.extract_sum(hxs.select('//div[@class="views-field-sum-1"]'))
        item['co_borrowers'] = co_borrowers
        item['co_borrowers_meta'] = co_borrowers_meta

        # Number of depositors
        co_depositors, co_depositors_meta = self.extract_sum(hxs.select('//div[@class="views-field-sum-4"]'))
        item['co_depositors'] = co_depositors
        item['co_depositors_meta'] = co_depositors_meta

        # Address (multiline)
        addr_lines = hxs.select('//div[@class="address-line"]')
        for lbl, addr in zip(['co_address1', 'co_address2', 'co_address3', 'co_address4', 'co_address5', 'co_address6'], addr_lines):
            tmp = addr.select('text()').extract()
            if tmp != []:
                item[lbl] = tmp[0]

        return item
