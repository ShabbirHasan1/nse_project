import boto3
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client



def getLatestPrice(equityName) :
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}

    baseUrl = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='
    url = baseUrl + equityName
    print(url)
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    dataArray = soup.find(id='responseDiv').getText().strip().split(':')

    for item in dataArray:
        if 'lastPrice' in item:
            index = dataArray.row_index(item) + 1

    lastPrice = dataArray[index].split('"')
    return float(lastPrice[1].replace(',', ''))


dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table_name = 'Purchased-Shares'
table = dynamodb.Table(table_name)

result = table.scan()
equities = result['Items']
for equity in equities:
    equityName = equity['partition_key']
    latestPrice = getLatestPrice(equityName=equityName)

AccountSID = 'AC19460e393ee78da313b92a2156b487e1'
AuthToken = '59a42b278c17f1426bcdb01bc9d5a036'
client = Client(AccountSID, AuthToken)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919000017580'

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table_name = 'Purchased-Shares'
table = dynamodb.Table(table_name)

result = table.scan()
equities = result['Items']
for equity in equities:
    equityName = equity['partition_key']
    latestPrice = getLatestPrice(equityName=equityName)
    purchasedRate = float(equity['Purchase Rate'])
    percentChange = ((latestPrice - purchasedRate) / latestPrice) * 100
    print(equityName, percentChange)

    if percentChange <= -25.0:
        msg = equityName + ' Price reduced by 25%, better sell it'
        client.messages.create(body=msg,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)
    elif percentChange >= 10.0:
        msg = equityName + ' Price increased by 10%, it is good time to sell it'
        client.messages.create(body=msg,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)
