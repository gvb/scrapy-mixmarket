# Scrapy settings for mixmarket project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

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

