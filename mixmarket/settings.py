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

