from datetime import date
import scrapy
import hashlib
from ..items import CardekhoItem


class CarDekhoSpider(scrapy.Spider):
    name = 'car_dekho'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'CONCURRENT_REQUESTS': 2,
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        },
        "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_TIMEOUT": 600
    }
    allowed_domains = ['www.cardekho.com']
    start_urls = ['https://www.cardekho.com/usedCars']

    def hashID(self, stringInput):
        hashTool = hashlib.md5()
        hashTool.update(stringInput.encode())
        return hashTool.hexdigest()

    def parse(self, response):
        items = CardekhoItem()
        cars = response.css('.holder')
        for car in cars:
            selector = scrapy.Selector(text=car.get())
            car_title = selector.css('.title::text').get()
            price_blurb = selector.css('.price::text').extract().pop(1)
            fuel_type = selector.css('.dotlist span:nth-child(2)::text').get()
            gear_box = selector.css('span~ span+ span::text').get()
            variant = selector.css('div.variant::text').get()
            mileage = selector.css('.dotlist span:nth-child(1)::text').get()

            items['car_title'] = car_title
            items['price_blurb'] = price_blurb
            items['fuel_type'] = fuel_type
            items['gear_box'] = gear_box
            items['variant'] = variant
            items['mileage'] = mileage
            items['record_create_date'] = str(date.today())
            items['project_id'] = 'car123'
            items['site'] = 'www.cardekho.com'
            items['source_country'] = 'IND'
            yield items
