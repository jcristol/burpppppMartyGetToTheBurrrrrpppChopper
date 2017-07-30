from bs4 import BeautifulSoup
from pprint import pprint
from urllib2 import urlopen, urlretrieve
from re import search

baseUrl = 'http://rickandmorty.wikia.com'
mortyTableUrl = baseUrl + '/wiki/List_of_Mortys_(Pocket_Mortys)'

def soupify(url):
    response = urllib2.urlopen(url)
    return BeautifulSoup(response.read(), 'html.parser')

def searchForTables(soup):
    return [e for e in soup.descendants if e.name == "table"]

#base wiki page with all the morty table entries
soup = soupify(mortyTableUrl)
mortyTable = searchForTables(soup)[1]
mortyTableEntries = [tag for tag in mortyTable.descendants if tag.name == "a" and "href" in tag.attrs if re.search('^/wiki/\w+$', tag["href"])]

testTag = mortyTableEntries[0]

#inner morty image url
testUrl = baseUrl + testTag['href']
mortySoup = soupify(testUrl)
pocketMortyImageTable = searchForTables(mortySoup)[0]
imgTag = [tag for tag in pocketMortyImageTable.descendants if tag.name == "img" and "data-image-name" in tag.attrs and re.search('PM\-\d+\.png', tag["data-image-name"])][0]
srcImageUrl = imgTag["src"]
print srcImageUrl

#download the image
urllib2.urlretrieve(srcImageUrl, "test.png")





# PM-002.png

# for tag in mortyTableEntries:
#     url = baseUrl + tag['href']
#     print "requesting " + url
#     response = urllib2.urlopen(url)
#     print "responded with " + str(response.getcode())
#     print

# import code
# code.interact(local=locals())
