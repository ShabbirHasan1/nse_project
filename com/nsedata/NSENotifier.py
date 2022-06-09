from datetime import date, timedelta
from nsepy import get_history
from twilio.rest import Client
import nsepy as nse
import CourseraPython.com.nsedata.TimeComparison as timeComparison
import CourseraPython.com.nsedata.GSReader as gsReader
import math


def getLatestPrice(equity_name) :
    q = nse.get_quote(equity_name)
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


def fortNightDate():
    fort_night_date = date.today() - timedelta(days=30)
    return fort_night_date


def maxValue(price_list) :
    max_value = price_list[0]
    for value in price_list :
        if max_value < value :
            max_value = value
    return max_value


def populateMaxValues(shares_dict, share_names, start_date) :
    for equityName in share_names:
        data = get_history(symbol=equityName, start=start_date, end=date.today())
        high_vals = list(data['High'])
        print(equityName)
        max_val = maxValue(price_list=high_vals)
        shares_dict[equityName] = max_val


def informReducedShares(nse_share_names, msg_sent_status, purchased_shares, nse_shares_info_dict) :
    purchase_shares = dict()
    purchased_price = gsReader.getSharesPurchasedPrice()

    for equity_name in nse_share_names:
        print(equity_name)
        current_val = getLatestPrice(equity_name)
        equity_max_val = nse_shares_info_dict[equity_name]
        if equity_name in purchased_shares:
            if current_val < (purchased_price.get(equity_name,0) * 0.92):
                percentChange = round((equity_max_val - current_val) / equity_max_val * 100, 2)
                purchase_shares[equity_name] = str(percentChange) + ' && val : ' + str(current_val)
                msg_sent_status[equity_name] = True
            continue

        if current_val < equity_max_val * 0.90 :
            percentChange = round((equity_max_val - current_val) / equity_max_val * 100, 2)
            purchase_shares[equity_name] = str(percentChange) + ' && val : ' + str(current_val)
            msg_sent_status[equity_name] = True

    return purchase_shares


def getSellSharesInfo(sell_shares_msg_status, shares_exp_price):
    sell_shares = list()
    for equity_name in shares_exp_price.keys() :
        current_val = getLatestPrice(equity_name)
        if current_val > float(shares_exp_price[equity_name]) :
            #msg_sent_status = sell_shares_msg_status.get(equity_name, False)
            #if not msg_sent_status:
            sell_shares_msg_status[equity_name] = True
            sell_shares.append(equity_name)
    return sell_shares


def sendWhatsAppMsg(nifty50_purchased_shares):
    account_sid = 'AC19460e393ee78da313b92a2156b487e1'
    auth_token = '59a42b278c17f1426bcdb01bc9d5a036'
    client = Client(account_sid, auth_token)
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+919000017580'

    client.messages.create(body=str(nifty50_purchased_shares), from_=from_whatsapp_number, to=to_whatsapp_number)


startDate = fortNightDate()
nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'IRCTC']
#'INFRATEL'
nseFirst50SharesInfoDict = dict()
if len(nseFirst50SharesInfoDict.keys()) == 0 :
    populateMaxValues(nseFirst50SharesInfoDict, nseShareNames, startDate)

nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nseNext50SharesInfoDict = dict()
if len(nseNext50SharesInfoDict.keys()) == 0 :
    populateMaxValues(nseNext50SharesInfoDict, nseNext50shareNames, startDate)
#print(nseNext50SharesInfoDict)

sharesExpPrice = gsReader.getSharesExpectedPrice()

count = 0
nifty50MsgStatus = dict()
niftyNext50MsgStatus = dict()
sellSharesMsgStatus = dict()
while True :

    nifty50PurchasedShares = informReducedShares(nseShareNames, nifty50MsgStatus, sharesExpPrice.keys(),
                                                 nseFirst50SharesInfoDict)
    print('nifty50 : '+ str(nifty50PurchasedShares))
    #if len(nifty50PurchasedShares.keys()) != 0:
    msg = 'nifty50 : ' + str(nifty50PurchasedShares)
        #sendWhatsAppMsg('nifty50 : '+ str(nifty50PurchasedShares))

    niftyNext50PurchasedShares = informReducedShares(nseNext50shareNames, niftyNext50MsgStatus, sharesExpPrice.keys(),
                                                     nseNext50SharesInfoDict)
    print('niftyNext50 : '+ str(niftyNext50PurchasedShares))
    #if len(nifty50PurchasedShares.keys()) != 0:
    msg = msg + '\n' + 'niftyNext50 : '+ str(niftyNext50PurchasedShares)
        #sendWhatsAppMsg('niftyNext50 : '+ str(niftyNext50PurchasedShares))

    #sellShares = getSellSharesInfo(sellSharesMsgStatus, sharesExpPrice)
    #print('Sell ', sellShares)
    #if len(sellShares) != 0:
    #msg = msg + '\n' + 'Sell Shares : ' + str(sellShares)
        #sendWhatsAppMsg('Sell Shares : ' + str(sellShares))
    #sendWhatsAppMsg(msg)
    timeComparison.sleep10mins()
    if timeComparison.isClosingTime():
        break
