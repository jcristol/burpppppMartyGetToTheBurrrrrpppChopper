from bs4 import BeautifulSoup
from pprint import pprint
import re, urllib, urllib2

baseUrl = 'http://rickandmorty.wikia.com'
mortyTableUrl = baseUrl + '/wiki/List_of_Mortys_(Pocket_Mortys)'

def soupify(url):
    print "Request: " + url
    response = urllib2.urlopen(url)
    print "Responded: " + str(response.getcode())
    return BeautifulSoup(response.read(), 'html.parser')

def getPocketMortyImgUrlAndName(soup):
    pocketMortyImageTableList = [e for e in soup.descendants if e.name == "table" and "class" in e.attrs and len(e["class"]) == 1 and e["class"][0] == "infobox-interior"]
    if len(pocketMortyImageTableList) == 1:
        imgTagList = [tag for tag in pocketMortyImageTableList[0].descendants if tag.name == "img" and "data-image-name" in tag.attrs and re.search('PM\-\d+\.png', tag["data-image-name"])]
        if len(imgTagList) != 1:
            return (None, None)
        return (imgTagList[0]["src"], imgTagList[0]['data-image-name'])
    return (None, None)

def download(url, name):
    if url is None or name is None:
        return
    print "Request Download from: " + url
    urllib.urlretrieve(url, "images/" + name)
    print "Downloaded: " + name
    return



#base wiki page with all the morty table entries
soup = soupify(mortyTableUrl)
mortyTable = [e for e in soup.descendants if e.name == "table"][1]
mortyTableEntries = [tag for tag in mortyTable.descendants if tag.name == "a" and "href" in tag.attrs if re.search('^/wiki/\w+$', tag["href"])]
pocketMortyWikiUrls = [baseUrl + tag['href'] for tag in mortyTableEntries]
mortyWikiSoups = [soupify(url) for url in pocketMortyWikiUrls]
mortyImageUrlsAndNames = [getPocketMortyImgUrlAndName(soup) for soup in mortyWikiSoups]
[download(url, name) for url, name in mortyImageUrlsAndNames]
