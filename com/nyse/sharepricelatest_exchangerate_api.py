import requests

# This returns previous data

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/090930f831b1379498c1b217/latest/EUR'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)


