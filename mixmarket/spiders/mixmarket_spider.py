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

        # Portfolio has several pieces
        tmp = hxs.select('//div[@class="views-field-sum"]')
        # Numeric part, e.g "3.1".  We also need to strip the commas ","
        # out of the number before converting it to a float.
        co_po_str = tmp.select('span/span[@class="numeric"]/text()').extract()[0]
        co_portfolio = float(co_po_str.replace(",", ""))

        # Order part, e.g. "million"
        scale = tmp.select('span/span/span[@class="order"]/text()').extract()
        if scale != []:
            if scale[0] == u'thousand':
                co_portfolio = co_portfolio * 1000.0
            if scale[0] == u'million':
                co_portfolio = co_portfolio * 1000000.0
        item['co_portfolio'] = co_portfolio

        # Meta part, e.g. "USD, date"
        item['co_portfolio_meta'] = tmp.select('label/span[@class="meta"]/text()').extract()[0]

        return item
