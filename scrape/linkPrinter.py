from bs4 import BeautifulSoup
from pprint import pprint
import urllib2
import re

baseUrl = 'http://rickandmorty.wikia.com'
mortyListUrl = baseUrl + '/wiki/List_of_Mortys_(Pocket_Mortys)'

response = urllib2.urlopen(mortyListUrl)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

mortyTable = [e for e in soup.descendants if e.name == "table"][1]
mortyTags = [tag for tag in mortyTable.descendants if tag.name == "a" and "href" in tag.attrs if re.search('^/wiki/\w+$', tag["href"])]

for tag in mortyTags:
    url = baseUrl + tag['href']
    print "requesting " + url
    response = urllib2.urlopen(url)
    print "responded with " + str(response.getcode())
    print

# import code
# code.interact(local=locals())