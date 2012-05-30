# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
#
# Copyright (c) 2011,2012 Gerald Van Baren, gvb @ unssw.com
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
