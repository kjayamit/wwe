from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class wweSpider(Spider):
    name = "wwe"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_WWE_pay-per-view_events",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//table[@class="wikitable"]//tr/td[2]')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('../td[3]/a/text()').extract()
            item['description'] = site.xpath('../td[5]/a/text()')
            items.append(item)

        return items
