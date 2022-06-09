import urllib.request, urllib.parse, urllib.error
import json

Link = input('enter API URL: ')
url = urllib.request.urlopen(Link)
jsondata = url.read().decode()
data = json.loads(jsondata)
comments = data['comments']
sum = 0;
for comment in comments :
    sum = sum + comment['count']

print(sum)