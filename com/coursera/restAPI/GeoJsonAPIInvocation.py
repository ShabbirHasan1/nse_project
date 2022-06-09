import urllib.request, urllib.parse, urllib.error
import json

location = input('Enter location:')

url = 'http://py4e-data.dr-chuck.net/json?'
newUrl = url + urllib.parse.urlencode({'address': location})
print(newUrl)
jsonObj = urllib.request.urlopen(newUrl)
#data = json.loads(jsonObj)

print(jsonObj)
