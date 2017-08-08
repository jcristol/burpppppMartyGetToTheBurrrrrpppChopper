# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

<<<<<<< HEAD:pokedex/pokedexCrawlers/pokedexCrawlers/spiders/mortyCrawler.py
class MortycrawlerSpider(CrawlSpider):
    name = 'mortyCrawler'
=======
#helper functions
def evoDicts(soup):
    res = []
    allLinks = soup.find_all('a')
    for link in allLinks:
        img = link.img
        res.append({'link' : img["data-src"]})
    return res

class MySpider(CrawlSpider):
    name = 'morty'
>>>>>>> edfaa62dd7c7c1c3e359f94bb288be03cc493655:pokedex/mortyCrawl/mortyCrawl/spiders/morty.py
    start_urls = ["http://rickandmorty.wikia.com/wiki/List_of_Mortys_(Pocket_Mortys)"]
    rules = (
        Rule(LinkExtractor(allow=('wiki/.*Morty$', )), callback='parse_item'),
    )

    def parse_item(self, response):
        #would like to rewrite the parser using after extracting big dom elements
        self.logger.info('A page! %s', response.url)
        title = response.css('h1[class="page-header__title"]::text').extract_first()
        quote = response.css('i::text').extract_first()
        infoBoxHTML = response.css('table[class="infobox-interior"][cellspacing]').extract_first()
        tableRowSoups = BeautifulSoup(infoBoxHTML, 'html.parser').find_all('tr')

        #info box specfic soups
        titleSoup = tableRowSoups[0]
        topLilIconSoup = tableRowSoups[1]
        bigImageSoup = tableRowSoups[2]
        basicInfoBarSoup = tableRowSoups[3]
        typeSoup = tableRowSoups[4]
        bodyInfoSoup = tableRowSoups[5]
        characteristicsSoup = tableRowSoups[6]
        evolutionBarSoup = tableRowSoups[7]
        evolutionSoup = tableRowSoups[8]
        campaignInfoBarSoup = tableRowSoups[9]
        campaignInfoSoup = tableRowSoups[10]
        multiPlayerBarSoup = tableRowSoups[11]
        multiPlayerInfo1Soup = tableRowSoups[12]
        multiPlayerInfo2Soup = tableRowSoups[13]

        #yield json of morty info
        yield {
            'article' : {'title' : title.strip(), 'quote' : quote.strip()},
            'lil_icon' : {'file_name' : topLilIconSoup.img["data-image-name"].strip().strip("\""), 'src' : topLilIconSoup.img["src"].strip().strip("\"")},
            'big_image' : {'file_name' : bigImageSoup.img["data-image-name"].strip().strip("\""), 'src' : bigImageSoup.img["src"].strip().strip("\"")},
            'basic_info' : {
                'type_info' : {'name' : typeSoup.img['alt'].strip().strip("\""), 'file_name' : typeSoup.img["data-image-key"].strip().strip("\""), 'src' : typeSoup.img['src'].strip().strip("\"")},
                'body_info' : {'height' : bodyInfoSoup.td.next_sibling.text.strip().strip("\""), 'weight' : bodyInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
            },
<<<<<<< HEAD:pokedex/pokedexCrawlers/pokedexCrawlers/spiders/mortyCrawler.py
=======
            'evolution_info' : evoDicts(evolutionSoup),
>>>>>>> edfaa62dd7c7c1c3e359f94bb288be03cc493655:pokedex/mortyCrawl/mortyCrawl/spiders/morty.py
            'campaign_info' : {'badges_req' : campaignInfoSoup.td.next_sibling.text.strip().strip("\""), 'rare' : campaignInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
        }
