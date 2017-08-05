# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class SoundcrawlerSpider(CrawlSpider):
    name = 'soundCrawler'
    start_urls = ['https://peal.io/soundboards/rick-and-morty']

    def parse(self, response):
        players = response.css('audio.player')
        grossLinks = players.css('source').extract()
        prettyLinks = []
        for link in grossLinks:
            soup = BeautifulSoup(link, 'html.parser')
            prettyLinks.append(soup.source['src'])
        yield {
            'links' : prettyLinks
        }
