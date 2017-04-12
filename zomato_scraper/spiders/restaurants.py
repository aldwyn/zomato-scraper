# -*- coding: utf-8 -*-
import json
import re
import scrapy
from scrapy.loader import ItemLoader

from zomato_scraper.items import Restaurant


class RestaurantsSpider(scrapy.Spider):
    name = "restaurants"
    start_urls = [
        'https://www.zomato.com/cebu/24-hour-restaurant',
        'https://www.zomato.com/cebu/all-you-can-eat',
        'https://www.zomato.com/cebu/amazing-ribs',
        'https://www.zomato.com/cebu/artisan-bakeries',
        'https://www.zomato.com/cebu/best-burger',
        'https://www.zomato.com/cebu/best-cheesecake',
        'https://www.zomato.com/cebu/best-coffee',
        'https://www.zomato.com/cebu/best-japanese-food',
        'https://www.zomato.com/cebu/best-new-restaurants',
        'https://www.zomato.com/cebu/best-steak',
        'https://www.zomato.com/cebu/cheap-eats',
        'https://www.zomato.com/cebu/cityscapes',
        'https://www.zomato.com/cebu/fine-dining-restaurants',
        'https://www.zomato.com/cebu/graduation-specials',
        'https://www.zomato.com/cebu/hidden-restaurants',
        'https://www.zomato.com/cebu/homegrown-restaurants',
        'https://www.zomato.com/cebu/insta-worthy-places',
        'https://www.zomato.com/cebu/pasta',
        'https://www.zomato.com/cebu/romantic-restaurants',
        'https://www.zomato.com/cebu/seafood',
        'https://www.zomato.com/cebu/top-restaurants',
    ]

    def parse(self, response):
        selector = 'div.collection_listings_container div.top-res-box'
        for resto in response.css(selector):
            url = resto.css('a.top-res-box-bg::attr(href)').extract_first()
            import logging
            logging.info(url)
            if 'filterby_collection_id' in url:
                yield scrapy.Request(url, callback=self.parse_collection_page)
            else:
                yield scrapy.Request(url, callback=self.parse_items)

    def parse_collection_page(self, response):
        for resto_href in response.css('a.result-title::attr(href)').extract():
            yield scrapy.Request(resto_href, callback=self.parse_items)

    def parse_items(self, response):
        loader = ItemLoader(item=Restaurant(), response=response)
        loader.add_css('id', '[data-res-id]::attr(data-res-id)')
        loader.add_css('name', 'meta[property="og:title"]::attr(content)')
        loader.add_css('description', 'meta[name="twitter:description"]::attr(content)')
        loader.add_css('address', 'div.res-main-address span::text')
        loader.add_css('thumbnail', 'meta[name="twitter:image"]::attr(content)')
        loader.add_css('creator', 'meta[name="twitter:creator"]::attr(content)')
        loader.add_css('url', 'meta[property="og:url"]::attr(content)')
        loader.add_css('latitude', 'meta[property="place:location:latitude"]::attr(content)')
        loader.add_css('longitude', 'meta[property="place:location:longitude"]::attr(content)')
        loader.add_css('cuisines', 'div.res-info-cuisines > a::text')
        loader.add_css('highlights', 'div.res-info-highlights > div.res-info-feature-text::text')
        loader.add_css('type', 'span.res-info-estabs > a.grey-text::text')
        loader.add_css('known_for', 'div.res-info-known-for-text::text')

        def format_result(selector, to_replace):
            res = response.css(selector).extract_first()
            res = res.replace(to_replace, '').strip() if res else None
            res = res.replace(to_replace.strip('s'), '').strip() if res else None
            return res

        loader.add_value('rating',
                         format_result('meta[property="zomatocom:average_rating"]::attr(content)', 'Rating: '))
        loader.add_value('reviews_count',
                         format_result('meta[property="zomatocom:user_reviews"]::attr(content)', ' Reviews'))

        menu_url = response.css('div.respageMenu > a[href$="menu"]::attr(href)').extract_first()
        request = scrapy.Request(menu_url, self.parse_menu_urls)
        request.meta['item'] = loader.load_item()
        yield request

    def parse_menu_urls(self, response):
        item = response.meta['item']
        for script in response.css('script[type="text/javascript"]::text').extract():
            menu_pages = re.search(r'zomato\.menuPages = (.*?)\;', script)
            if menu_pages:
                menu_pages = json.loads(menu_pages.group(1))
                item['menu_urls'] = [u['href'] for u in menu_pages]
                break
        yield item
