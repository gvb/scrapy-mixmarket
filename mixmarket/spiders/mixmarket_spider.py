from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class MixMarketSpider(BaseSpider):
    name = "mixmarket"
    allowed_domains = ["mixmarket.org"]
    start_urls = [
        "http://mixmarket.org/mfi/country/Afghanistan"
    ]

    def parse(self, response):
#        filename = response.url.split("/")[-1]	# country, with no trailing '/'
#        open(filename, 'wb').write(response.body)
        hxs = HtmlXPathSelector(response)

        # The company info is saved in table rows
        company_rows = hxs.select('//tr')
        for company_row in company_rows:
            institution = company_row.select('td[@class="views-field views-field-name active"]/a/text()').extract()
            details_link = company_row.select('td[@class="views-field views-field-name active"]/a/@href').extract()
            date = company_row.select('td[@class="views-field views-field-as-of-date"]/text()').extract()
            rating = company_row.select('td[@class="views-field views-field-flatstore-mfi-mfdb-data-mix-diamonds--c"]/a/span/text()').extract()
            portfolio = company_row.select('td[@class="views-field views-field-balance-sheet-usd-gross-loan-portfolio"]/span/text()').extract()
            borrowers = company_row.select('td[@class="views-field views-field-products-and-clients-total-borrowers"]/span/text()').extract()
            #= company_row.select('td[@class=""]/text()').extract()

            # We rows from other tables, drop the extra rows
            if institution != []:
                print institution, details_link, date, rating, portfolio, borrowers


#        # companies will be an array of links: u'<a href="/mfi/afs">AFS</a>'
#        companies = hxs.select('//td[@class="views-field views-field-name active"]/a')
#        company_dates = hxs.select('//td[@class="views-field views-field-as-of-date"]/a')
#        for company in companies:
#            institution = company.select('text()').extract()
#            details_link = company.select('@href').extract()
#            print institution, details_link
