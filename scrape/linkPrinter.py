from bs4 import BeautifulSoup
from pprint import pprint
import urllib2
import re

baseUrl = 'http://rickandmorty.wikia.com'
mortyTableUrl = baseUrl + '/wiki/List_of_Mortys_(Pocket_Mortys)'

def soupify(url):
    response = urllib2.urlopen(url)
    return BeautifulSoup(response.read(), 'html.parser')

soup = soupify(mortyTableUrl)
mortyTable = [e for e in soup.descendants if e.name == "table"][1]
mortyTableEntries = [tag for tag in mortyTable.descendants if tag.name == "a" and "href" in tag.attrs if re.search('^/wiki/\w+$', tag["href"])]

testTag = mortyTableEntries[0]

url = baseUrl + testTag['href']
mortySoup = soupify(url)
print mortySoup.prettify()




# for tag in mortyTableEntries:
#     url = baseUrl + tag['href']
#     print "requesting " + url
#     response = urllib2.urlopen(url)
#     print "responded with " + str(response.getcode())
#     print

# import code
# code.interact(local=locals())
