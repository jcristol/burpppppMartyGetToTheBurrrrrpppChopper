import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'morty'
    start_urls = ["http://rickandmorty.wikia.com/wiki/List_of_Mortys_(Pocket_Mortys)"]
    rules = (
        Rule(LinkExtractor(allow=('wiki/.*Morty$', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('A page! %s', response.url)
        title = response.css('h1[class="page-header__title"]::text')
        article = response.css('article[id="WikiaMainContent"]')
        yield {
            'title' : title.extract()
        }
