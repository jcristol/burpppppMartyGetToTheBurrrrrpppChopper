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
        quote = response.css('i::text')
        infoBox = article.css('table[class="infobox-interior"]')
        trs = infoBox.css('tr')
        imageBox = trs[2]
        typeInfo = trs[4]
        sizeInfo = trs[5]
        charInfo = trs[6]
        lilMorty = trs[8]
        campInfo = trs[10]
        yield {
            'morty_page' : {
                'title' : title.extract_first(),
                'quote' : quote.extract_first(),
                'bigImageLink' : imageBox.css('a::attr(href)').extract_first(),
                'type' : typeInfo.css('a::attr(href)').extract_first(),
                'height' : sizeInfo.css('td:nth-of-type(2)::text').extract_first(),
                'weight' : sizeInfo.css('td:nth-of-type(4)::text').extract_first(),
                'characteristics' : charInfo.css('td:nth-of-type(2)::text').extract_first(),
                # 'lilImageLink' : lilMorty.css('a::attr(href)').extract_first()
            }
        }
