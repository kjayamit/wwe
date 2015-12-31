from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    venue = Field()
    url = Field()

class Website2(Item):

    name = Field()
    stipulation = Field()