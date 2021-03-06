# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class ExpansysComSgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    description = Field()
    retailer_sku_code = Field()
    model = Field()
    mpn = Field()
    sku = Field()
    upc = Field()
    ean = Field()
    currency = Field()
    price = Field()
    crawl_time = Field()
    promo_price = Field()
    promo_qty = Field()
    promo_data = Field()
    promo_expiry = Field()
    current_price = Field()
    brand = Field()
    primary_image_url = Field()
    image_urls = Field()
    categories = Field()
    attributes = Field()
    features = Field()
    rating = Field()
    rating = Field()
    instock = Field()
