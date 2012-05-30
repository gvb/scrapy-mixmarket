# Scrapy settings for mixmarket project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
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

BOT_NAME = 'mixmarket'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mixmarket.spiders']
NEWSPIDER_MODULE = 'mixmarket.spiders'
DEFAULT_ITEM_CLASS = 'mixmarket.items.MixmarketItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# Output file and format
FEED_URI = 'mixmarket.csv'
FEED_FORMAT = 'csv'

FEED_EXPORTERS = {
    'csv': 'mixmarket.feedexport.CSVkwItemExporter'
}

# By specifying the fields to export, the CSV export honors the order
# rather than using a random order.
EXPORT_FIELDS = [
    'country',
    'co_name',
    'co_date_inc',
    'co_rating',
    # Gross loan portfolio, metadata (e.g. "USD, 2009")
    'co_portfolio',      
    'co_portfolio_meta', 
    # Assets
    'co_assets',         
    'co_assets_meta',    
    # Deposits
    'co_deposits',       
    'co_deposits_meta',  
    # Number of active borrowers
    'co_borrowers',      
    'co_borrowers_meta', 
    # Number of depositors
    'co_depositors',     
    'co_depositors_meta', 

    'co_address1',
    'co_address2',
    'co_address3',
    'co_address4',
    'co_address5',
    'co_address6',
    'co_phone',
    'co_email',
    'co_website',
#    fundingsrc',
#    products_svcs',
#    looking_for',
    'co_percent_ops_mf_min',
    'co_percent_ops_mf_max',
    'co_established',
    'co_fye',
    'co_legal_status',
    'co_regulated',
]

