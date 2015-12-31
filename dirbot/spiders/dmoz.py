from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request

from dirbot.items import Website
from dirbot.items import Website2


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
            item['venue'] = site.xpath('../td[3]/a/text()').extract()
            # item['url'] = site.xpath('a/@href').extract()
            item['url'] = "https://en.wikipedia.org" + str(site.xpath('a/@href').extract())
            print 'Something something ', item['url']
            item['description'] = site.xpath('../td[5]/a/text()')
            request = Request(item['url'],
                              callback=self.parse_page2)
            items.append(item)

        return items

    def parse_page2(self, response):

        sel = Selector(response)
        sites = sel.xpath('//table[@class="wikitable"]//tr')
        items = []



        for site in sites:
            item = Website2()
            item['name'] = site.xpath('td[1]/a/text()').extract()
            item['stipulation'] = site.xpath('td[1]/text()').extract()

        return items
