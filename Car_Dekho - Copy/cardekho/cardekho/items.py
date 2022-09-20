import scrapy

class CardekhoItem(scrapy.Item,object):
    # define the fields for your item here like:

    car_title = scrapy.Field()
    price_blurb = scrapy.Field()
    fuel_type = scrapy.Field()
    gear_box = scrapy.Field()
    variant = scrapy.Field()
    mileage = scrapy.Field()
    record_create_date = scrapy.Field()
    project_id = scrapy.Field()
    source_country = scrapy.Field()
    site = scrapy.Field()




    # Make_year = scrapy.Field()
    # Engine = scrapy.Field()
    # Reg_year = scrapy.Field()
    # fuel = scrapy.Field()
    # Kms_driven = scrapy.Field()
    # No_of_owner = scrapy.Field()
    # transmission = scrapy.Field()
    # torque = scrapy.Field()
    pass
