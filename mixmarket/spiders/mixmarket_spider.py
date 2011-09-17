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

        # The institution is in the page title
        item['co_name'] = hxs.select('//title').extract()
        item['co_date_inc'] = hxs.select('//div[@class="field field-type-date field-field-mfi-date"]/div/div/span/text()').extract()
        item['co_rating'] = []
        for diamonds in range(5):
            co_rating = hxs.select("//span[@class=\"diamonds diamonds-%d\"]/text()" % diamonds).extract()
            if co_rating != []:
                item['co_rating'] = co_rating
                break
        # Portfolio has several pieces
        tmp = hxs.select('//div[@class="views-field-sum"]')
        # Numeric part, e.g "3.1"
        co_portfolio = tmp.select('span/span[@class="numeric"]/text()').extract()
        # Order part, e.g. "million"
        co_portfolio.append(tmp.select('span/span/span[@class="order"]/text()').extract())
        # Meta part, e.g. "USD, date"
        co_portfolio.append(tmp.select('label/span[@class="meta"]/text()').extract())
        item['co_portfolio'] = co_portfolio




        print item

        return item
