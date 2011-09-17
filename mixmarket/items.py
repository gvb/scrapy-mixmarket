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
    co_portfolio = Field()	# Gross loan portfolio
    co_borrowers = Field()	# Number of active borrowers
#    deposits = Field();
#    num_depositors = Field();
#    total_assets = Field();
#    mission = Field();
#    address = Field();		# Multi-line represented as an array
#    phone = Field();
#    email = Field();
#    website = Field();
#    fundingsrc = Field();
#    products_svcs = Field();
#    looking_for = Field();
#    percent_ops_mf = Field();
#    established = Field();
#    fye = Field();
#    legal_status = Field();
#    regulated = Field();
#    partnerships = Field();	# Array of [organization, relationship]
