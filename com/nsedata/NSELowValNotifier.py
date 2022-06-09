import nsepy as nse
import nsedata.GSReader as gsReader
import nsedata.TimeComparison as timeComparison
from twilio.rest import Client


def getLatestPrice(equity_name) :
    q = nse.get_quote(equity_name)
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


def informReducedShares(nse_share_names, msg_sent_status, nse_shares_info_dict, nse_reduced_percent_info) :
    purchase_shares = dict()

    for equity_name in nse_share_names:
        #print(equity_name)
        current_val = getLatestPrice(equity_name)
        equity_least_val = nse_shares_info_dict[equity_name]
        equity_reduced_percent = nse_reduced_percent_info[equity_name]

        if ((current_val <= equity_least_val * 1.02 and equity_reduced_percent >= 20) or
            (current_val <= equity_least_val * 1.03 and equity_reduced_percent >= 21) or
            (current_val <= equity_least_val * 1.04 and equity_reduced_percent >= 22) or
            (current_val <= equity_least_val * 1.05 and equity_reduced_percent >= 25) or
            (current_val <= equity_least_val * 1.06 and equity_reduced_percent >= 26)) :

            purchase_shares[equity_name] = ' val : ' + str(current_val) + ' & Least Val : ' + str(equity_least_val) + \
                                       ' & Reduced% ' + str(equity_reduced_percent)

        #if current_val <= equity_least_val * 1.02:

            msg_sent_status[equity_name] = True
    return purchase_shares


def sendWhatsAppMsg(nifty50_purchased_shares):
    account_sid = 'AC19460e393ee78da313b92a2156b487e1'
    auth_token = '59a42b278c17f1426bcdb01bc9d5a036'
    client = Client(account_sid, auth_token)
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+919000017580'

    client.messages.create(body=str(nifty50_purchased_shares), from_=from_whatsapp_number, to=to_whatsapp_number)


sharesLeastPriceInfo = gsReader.getSharesLeastPriceInfo()
sharesReducedPercentInfo = gsReader.getSharesReducedPercentInfo()
nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL']


nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nse_midcap_data = ['PRESTIGE', 'GMRINFRA', 'APOLLOHOSP', 'TATACOMM', 'FRETAIL', 'IDBI', 'SUPREMEIND', 'M%26MFIN',
                   'ESCORTS', 'RAMCOCEM', 'SAIL', 'APOLLOTYRE', 'MPHASIS', 'ASHOKLEY', 'BHEL', 'SCHAEFFLER',
                   'JINDALSTEL', 'CHOLAFIN', 'ISEC', 'NAM-INDIA', 'EMAMILTD', 'BHARATFORG', 'HUDCO',
                   'SUNTV', 'QUESS', 'L%26TFH', 'VBL', 'IDFCFIRSTB', 'SUMICHEM', 'TVSMOTOR', 'CESC', 'DALBHARAT',
                   'MFSL', 'CROMPTON', 'AARTIIND',  'THERMAX', 'ERIS', 'GODREJAGRO',
                   'IOB', 'AUBANK', 'HAL', 'CUMMINSIND', 'MRPL', 'LTTS', 'RBLBANK', 'TTKPRESTIG', 'SUNDRMFAST',
                   'TATACONSUM', 'APLLTD', 'AMARAJABAT', 'NATIONALUM', 'ATUL', 'CASTROLIND', 'BAYERCROP',
                   'GODREJPROP', 'ALKEM', 'JUBLFOOD', 'CANBK', 'GLAXO', 'ADANIGAS', 'JKCEMENT', 'HEXAWARE',
                   'ADANIPOWER', 'IBVENTURES', 'CREDITACC', 'MRF', 'MOTILALOFS', 'UCOBANK', 'LICHSGFIN',
                   'FORTIS', 'SHRIRAMCIT', 'INDHOTEL', 'SYMPHONY', 'SYNGENE', 'JSWENERGY', 'GILLETTE', 'GUJGASLTD',
                   'ABB', 'ASTRAL', 'SUNDARMFIN', 'GODREJIND', 'NLCINDIA', 'SRF', 'WABCOINDIA',
                   'CHOLAHLDNG', 'CENTRALBK', 'HONAUT', 'POLYCAB', 'TORNTPOWER', 'PIIND', '3MINDIA', 'ENDURANCE',
                   'EXIDEIND', 'MANAPPURAM', 'MINDTREE', 'IPCALAB', 'VINATIORGA', 'TRENT', 'LALPATHLAB',
                   'SJVN', 'LTI', 'JUBILANT', 'SOLARINDS', 'NIACL', 'MGL', 'WHIRLPOOL', 'NATCOPHARM', 'RECLTD',
                   'BLUEDART', 'BALKRISIND', 'BANKINDIA', 'VGUARD', 'EIHOTEL', 'FEDERALBNK', 'GLENMARK', 'HATSUN',
                   'CUB', 'BATAINDIA', 'PFIZER', 'KANSAINER', 'TATAPOWER', 'OIL', 'PHOENIXLTD', 'ADANIGREEN',
                   'RAJESHEXPO', 'GSPL', 'AAVAS', 'RELAXO', 'IIFLWAM', 'VOLTAS', 'UNIONBANK', 'ABCAPITAL', 'SANOFI',
                   'ABFRL', 'PNBHOUSING', 'CRISIL', 'MINDAIND', 'COROMANDEL', 'AJANTPHARM', 'OBEROIRLTY', 'AIAENG',
                   'BEL', 'SKFINDIA', 'EDELWEISS']
#'NIITTECH', 'AKZOINDIA',
nifty50MsgStatus = dict()
niftyNext50MsgStatus = dict()
niftyMidCapMsgStatus = dict()

while True :

    nifty50PurchasedShares = informReducedShares(nseShareNames, nifty50MsgStatus, sharesLeastPriceInfo,
                                                 sharesReducedPercentInfo)
    print('nifty50 : '+ str(nifty50PurchasedShares))
    #msg = 'nifty50 : ' + str(nifty50PurchasedShares)

    niftyNext50PurchasedShares = informReducedShares(nseNext50shareNames, niftyNext50MsgStatus, sharesLeastPriceInfo,
                                                     sharesReducedPercentInfo)
    print('niftyNext50 : ' + str(niftyNext50PurchasedShares))
    #msg = msg + '\n' + 'niftyNext50 : ' + str(niftyNext50PurchasedShares)

    niftyMidcapPurchasedShares = informReducedShares(nse_midcap_data, niftyMidCapMsgStatus, sharesLeastPriceInfo,
                                                     sharesReducedPercentInfo)
    print('niftyMidcapData : ' + str(niftyMidcapPurchasedShares))
    #msg = msg + '\n' + 'niftyMidCap : ' + str(niftyMidcapPurchasedShares)

    #sendWhatsAppMsg(msg)
    timeComparison.sleep10mins()
    if timeComparison.isClosingTime():
        break
#print(sharesLeastPriceInfo)