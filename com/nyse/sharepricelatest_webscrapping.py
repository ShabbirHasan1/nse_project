import requests
from bs4 import BeautifulSoup

# this is not producing latest data

def get_headers():
    return {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
            "cache-control": "max-age=0",
            "dnt": "1",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

url = ('https://finance.yahoo.com/quote/EURUSD=X?p=EURUSD')

r = requests.get(url, headers=get_headers())
web_content = BeautifulSoup(r.text, 'lxml')
#print(web_content)
web_content = web_content.find('div', {"class" : "smartphone_Mt(6px)"})
print(web_content)
#web_content = web_content.find('div', {"class" : "D(ib) Mend(20px)"})
web_content = web_content.find('span').text

print(web_content)
#web_content = web_content.find('span', {"class" : "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
#print(web_content)
#print(r.text)