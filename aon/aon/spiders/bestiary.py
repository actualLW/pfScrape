import scrapy

class BestiarySpider(scrapy.Spider):
    name = "bestiary"
    start_urls = [
        'http://aonprd.com/Monsters.aspx?Letter=All',
    ]

    def parse(self, response):
        for row in response.xpath('//*[@id="ctl00_MainContent_GridView6"]//tr'):
            yield {
                'name' : row.xpath('td[1]//text()').extract_first(),
                'cr' : row.xpath('td[2]//text()').extract_first(),
                'type' : row.xpath('td[3]//text()').extract_first(),
                'environment' : row.xpath('td[4]//text()').extract_first(),
            }
