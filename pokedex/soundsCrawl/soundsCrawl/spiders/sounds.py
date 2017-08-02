import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class SoundsSpider(scrapy.Spider):
    name = 'sounds'
    start_urls = ['https://peal.io/soundboards/rick-and-morty']
    rules = (
        Rule(LinkExtractor(allow=('.*sound.peal.io/ps/audios.*\.wav.*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        pass
