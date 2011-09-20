# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MixmarketItem(Item):
    country = Field()
    co_name = Field()
    co_date_inc = Field()	# Date of incorporation
    co_rating = Field()		# "diamonds"
    # Gross loan portfolio, metadata (e.g. "USD, 2009")
    co_portfolio = Field()
    co_portfolio_meta = Field()
    # Assets
    co_assets = Field()
    co_assets_meta = Field()
    # Deposits
    co_deposits = Field()
    co_deposits_meta = Field()
    # Number of active borrowers
    co_borrowers = Field()
    co_borrowers_meta = Field()
    # Number of depositors
    co_depositors = Field()
    co_depositors_meta = Field()

    co_address1 = Field()
    co_address2 = Field()
    co_address3 = Field()
    co_address4 = Field()
    co_address5 = Field()
    co_address6 = Field()

    co_phone = Field()
    co_email = Field()
    co_website = Field()
#    fundingsrc = Field()
#    products_svcs = Field()
#    looking_for = Field()
    co_percent_ops_mf_min = Field()
    co_percent_ops_mf_max = Field()
    co_established = Field()
    co_fye = Field()
    co_legal_status = Field()
    co_regulated = Field()
#    partnerships = Field()
