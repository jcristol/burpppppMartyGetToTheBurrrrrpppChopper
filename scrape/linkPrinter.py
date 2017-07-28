from bs4 import BeautifulSoup
import urllib2
import re

def pprint(l):
    for e in l:
        print e


base_url = 'http://rickandmorty.wikia.com/wiki/List_of_Mortys_(Pocket_Mortys)'

response = urllib2.urlopen(base_url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

# '^/wiki/.*morty$'

mortyTable = [e for e in soup.descendants if e.name == "table"][1]
hrefATags = [e for e in mortyTable.descendants if e.name == "a" and "href" in e.attrs]
mortyTags = [tag for tag in hrefATags if re.search('^/wiki/\w*$', tag['href'])]

pprint(mortyTags)
