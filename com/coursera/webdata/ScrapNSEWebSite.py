import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}

baseUrl = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='
url = baseUrl + 'ABBOTINDIA'

html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')
dataArray = soup.find(id='responseDiv').getText().strip().split(':')

for item in dataArray:
    if 'lastPrice' in item:
        index = dataArray.row_index(item) + 1

lastPrice = dataArray[index].split('"')
print(float(lastPrice[1].replace(',', '')))