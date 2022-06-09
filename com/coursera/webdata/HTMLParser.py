import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    newUrl = tag.get('href')
    if newUrl is not None:
        print(newUrl)
        try :
            newhtml = urllib.request.urlopen(newUrl).read()
        except:
            continue
        newsoup = BeautifulSoup(newhtml, 'html.parser')
        newtags = newsoup('a')
        for newtag in newtags :
            tags.append(newtag)
