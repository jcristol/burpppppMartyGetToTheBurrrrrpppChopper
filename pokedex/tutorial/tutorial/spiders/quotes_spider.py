import scrapy


class QuotesSpider(scrapy.Spider):
    base_url = "http://rickandmorty.wikia.com/"
    name = "morty"
    start_urls = [
        "http://rickandmorty.wikia.com/wiki/List_of_Mortys_(Pocket_Mortys)"
    ]
    homeCrawled = False

    def homeCrawler(self, response):
        if self.homeCrawled:
            return
        for page in response.css('h1[class="page-header__title"]::text'):
            title = page.extract()
            if type(title) is unicode and title == "List of Mortys (Pocket Mortys)":
                for table in response.css('table[class="wikitable sortable"]'):
                    self.links = table.css('a[href$="Morty"]').css('a::attr(href)')
                    self.homeCrawled = True



    def parse(self, response):
        # for table in response.css('table[class="wikitable sortable"]'):
        #     yield {
        #         'links' : table.css('a[href$="Morty"]').extract()
        #     }
        # next_page
        # links = []
        # for table in response.css('table[class="wikitable sortable"]'):
        #     links = table.css('a[href$="Morty"]').css('a::attr(href)')
        # next_page = links.extract_first()
        # print "yo"
        # print next_page
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     print "hmm"
        #     print next_page
        #     yield scrapy.Request(next_page, callback=self.parse)


        #home page crawler collect all relevant links
        self.homeCrawler(response)
        #call a morty page crawler on each link

        #next page to crawl logic
        if self.links:
            next_page = self.links.extract_first()
            import code
            code.interact()
        else:
            yield{
                #all the stuff
            }
