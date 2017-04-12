# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst


class Restaurant(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    description = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    creator = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    address = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join()
    )
    url = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    thumbnail = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    reviews_count = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    rating = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    latitude = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    longitude = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    type = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    known_for = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst()
    )
    cuisines = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
    )
    highlights = scrapy.Field()
    menu_urls = scrapy.Field()
