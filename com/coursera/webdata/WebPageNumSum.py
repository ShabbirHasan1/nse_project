import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_605442.html').read()
soup = BeautifulSoup(url, 'html.parser')
spantags = soup('span')
sum = 0
for spantag in spantags:
    sum = sum + int(spantag.contents[0])

print(sum)