# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import os, errno, shutil
#util functions
def make_dir(directory):
    try:
        os.makedirs(directory)
        print "success"
    except OSError as e:
        print "failure"
        if e.errno != errno.EEXIST:
            raise
        else:
            shutil.rmtree(directory)
            make_dir(directory)

make_dir('data')

def store_info(morty):
    name = morty['article']['title'].replace(" ", "_")
    mortyDir = 'data' + '/' + name
    make_dir(mortyDir)
    import code
    code.interact(local=locals())
    try:
        print "Downloading big image for %s" % name
        urllib.urlretrieve(morty["big_image"]["src"], mortyDir + "/big_image.png")
    except:
        "Fatal error could not download big image"
        shutil.rmtree(mortyDir)
        return
    try:
        print "Downloading icon image for %s" % name
        urllib.urlretrieve(morty["lil_icon"]["src"], mortyDir + "/icon.png")
    except:
        print "Error downloading icon image for %s" % name
    try:
        print "Downloading type image for %s" % name
        urllib.urlretrieve(morty['basic_info']['type_info']['src'], mortyDir + "/type.png")
    except:
        print "Error downloading type image for %s" % name
    jFile = open(mortyDir + "/info.json","w+")
    jFile.write(json.dumps(morty))


class MortycrawlerSpider(CrawlSpider):
    name = 'mortyCrawler'
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

        mortyInfo = {
            'article' : {'title' : title.strip(), 'quote' : quote.strip()},
            'lil_icon' : {'file_name' : topLilIconSoup.img["data-image-name"].strip().strip("\""), 'src' : topLilIconSoup.img["src"].strip().strip("\"")},
            'big_image' : {'file_name' : bigImageSoup.img["data-image-name"].strip().strip("\""), 'src' : bigImageSoup.img["src"].strip().strip("\"")},
            'basic_info' : {
                'type_info' : {'name' : typeSoup.img['alt'].strip().strip("\""), 'file_name' : typeSoup.img["data-image-key"].strip().strip("\""), 'src' : typeSoup.img['src'].strip().strip("\"")},
                'body_info' : {'height' : bodyInfoSoup.td.next_sibling.text.strip().strip("\""), 'weight' : bodyInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
            },
            'campaign_info' : {'badges_req' : campaignInfoSoup.td.next_sibling.text.strip().strip("\""), 'rare' : campaignInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
        }
        store_info(mortyInfo)
        #yield json of morty info
        yield {
            'article' : {'title' : title.strip(), 'quote' : quote.strip()},
            'lil_icon' : {'file_name' : topLilIconSoup.img["data-image-name"].strip().strip("\""), 'src' : topLilIconSoup.img["src"].strip().strip("\"")},
            'big_image' : {'file_name' : bigImageSoup.img["data-image-name"].strip().strip("\""), 'src' : bigImageSoup.img["src"].strip().strip("\"")},
            'basic_info' : {
                'type_info' : {'name' : typeSoup.img['alt'].strip().strip("\""), 'file_name' : typeSoup.img["data-image-key"].strip().strip("\""), 'src' : typeSoup.img['src'].strip().strip("\"")},
                'body_info' : {'height' : bodyInfoSoup.td.next_sibling.text.strip().strip("\""), 'weight' : bodyInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
            },
            'campaign_info' : {'badges_req' : campaignInfoSoup.td.next_sibling.text.strip().strip("\""), 'rare' : campaignInfoSoup.td.next_sibling.next_sibling.next_sibling.text.strip().strip("\"")}
        }
