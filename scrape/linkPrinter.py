from bs4 import BeautifulSoup
import urllib2
import re
import pprint


base_url = 'http://rickandmorty.wikia.com/wiki/List_of_Mortys_(Pocket_Mortys)'

response = urllib2.urlopen(base_url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

mortyTable = [e for e in soup.descendants if e.name == "table"][1]
mortyTags = [tag for tag in mortyTable.descendants if tag.name == "a" and "href" in tag.attrs if re.search('^/wiki/\w+$', tag["href"])]
pprint(mortyTags)
