from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from mixmarket.items import MixmarketItem


class MixMarketSpider(BaseSpider):
    name = "mixmarket"
    allowed_domains = ["mixmarket.org"]
    start_urls = [
        "http://mixmarket.org/mfi/country/Afghanistan",
        "http://mixmarket.org/mfi/country/Brazil",
    ]

    def extract_sum(self, piece):
        """ views-field-sum parsing
        These have a numeric part, an order part, and a meta part
        """
        # Numeric part, e.g "3.1".  We also need to strip the commas ","
        # out of the number before converting it to a float.
        tmp = piece.select('span/span[@class="numeric"]/text()').extract()
        if tmp != []:
            num = float(tmp[0].replace(",", ""))
        else:
            num = 0

        # Order part, e.g. "thousand" or "million"
        tmp = piece.select('span/span/span[@class="order"]/text()').extract()
        if tmp != []:
            if tmp[0] == u'thousand':
                num = num * 1000.0
            if tmp[0] == u'million':
                num = num * 1000000.0
        tmp = piece.select('label/span[@class="meta"]/text()').extract()
        if tmp != []:
            meta = tmp[0]
        else:
            meta = ''
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
        if co_date_inc != []:
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

        # Phone
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-phone"]/div/div/text()').extract()
        if tmp != []:
            item['co_phone'] = tmp[0]

        # email
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-email"]/div/div/span').extract()
        if tmp != []:
            # Extract and undo anti-spam obfuscation
            tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-email"]/div/div/span/span[@class="u"]/text()').extract()
            tmp_u = tmp[0].replace(" [dot] ", ".")
            tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-email"]/div/div/span/span[@class="d"]/text()').extract()
            tmp_d = tmp[0].replace(" [dot] ", ".")
            item['co_email'] = tmp_u + "@" + tmp_d

        # Web site
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-website"]/div/div/a/@href').extract()
        if tmp != []:
            item['co_website'] = tmp[0]

        # Percentage of operations comprised of MF
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-mf-operation"]/div/div/text()').extract()
        if tmp != []:
            # Split it if it is a range, otherwise min and max are the same
            if '-' in tmp[0]:
                item['co_percent_ops_mf_min'], item['co_percent_ops_mf_max'] = tmp[0].split( "-")
            else:
                item['co_percent_ops_mf_min'] = tmp[0]
                item['co_percent_ops_mf_max'] = tmp[0]

        # Date established
        tmp = hxs.select('//div[@class="field field-type-date field-field-mfi-date"]/div/div/span/text()').extract()
        if tmp != []:
            item['co_established'] = tmp[0]

        # Fiscal year end
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-fye"]/div[@class="field-items"]/div/text()').extract()
        if tmp != []:
            item['co_fye'] = tmp[0]

        # Legal status
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-legal-status"]/div/div/text()').extract()
        if tmp != []:
            item['co_legal_status'] = tmp[0]

        # Regulated?
        tmp = hxs.select('//div[@class="field field-type-text field-field-mfi-is-regulated"]/div/div/text()').extract()
        if tmp != []:
            item['co_regulated'] = tmp[0]

        return item
