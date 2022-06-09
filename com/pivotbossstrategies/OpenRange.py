import nsepy as nse
import datetime
from datetime import date, timedelta
from nsepy import get_history


def getEquityData(equity_name) :
 hour = datetime.datetime.now().hour
 minute = datetime.datetime.now().minute
 cpr_day = date.today() - timedelta(days=90)
 #if hour >= 15 and minute >= 30:
 # cpr_day = date.today()

 data = get_history(symbol=equity_name, start=cpr_day, end=date.today())
 return data


def printExtremeRangeDays(equityName) :
 data = getEquityData(equityName)
 index = 0
 day_low = 0
 day_high = 0

 for row in data.itertuples():
  if index == 0:
   pp = (row.High + row.Low + row.Close) / 3
   bc = (row.High + row.Low) / 2
   tc = (pp - bc) + pp
   R1 = 2 * pp - row.Low
   S1 = 2 * pp - row.High

   index = index + 1
   continue

  day_low = row.Low
  day_high = row.High

  index = index + 1
  if day_low != 0 and day_high != 0:
   #if row.Open >= S1 and row.Open <= R1:
    #print('With in value ', row.Index)

   if (row.Open < bc or row.Open > tc) and (day_low >= row.Open or day_high <= row.Open):
    print(equityName,  ' Out side value, But with in Range ', row.Index)
   if day_low > row.Open or day_high < row.Open:
    print('Extreme Range ', row.Index)

  pp = (row.High + row.Low + row.Close) / 3
  bc = (row.High + row.Low) / 2
  tc = (pp - bc) + pp
  R1 = 2 * pp - row.Low
  S1 = 2 * pp - row.High


def getPPVal(cpr_data) :
 pp = (cpr_data['High'] + cpr_data['Low'] + cpr_data['Close']) / 3
 print(pp)
 return round(pp.__float__(), 2)


def getBCVal(data) :
 bc = (data['High'] + data['Low']) / 2
 return round(bc.__float__(), 2)


def getTCVal(data) :
 pp = (data['High'] + data['Low'] + data['Close']) / 3
 bc = (data['High'] + data['Low']) / 2
 tc = (pp - bc) + pp
 return round(tc.__float__(), 2)

def getR1Val(data) :
 pp = (data['High'] + data['Low'] + data['Close']) / 3
 R1 = 2 * pp - data['Low']
 return round(R1.__float__(), 2)


def getR2Val(data) :
 pp = (data['High'] + data['Low'] + data['Close']) / 3
 R2 = pp + data['High'] - data['Low']
 return round(R2.__float__(), 2)


def getR3Val(data):
 pp = (data['High'] + data['Low'] + data['Close']) / 3
 R3 = data['High'] + 2 * (pp - data['Low'])
 return round(R3.__float__(), 2)


def getS1Val(data) :
  pp = (data['High'] + data['Low'] + data['Close']) / 3
  S1 = 2 * pp - data['High']
  return round(S1.__float__(), 2)


def getS2Val(data):
 pp = (data['High'] + data['Low'] + data['Close']) / 3
 S2 = pp - data['High'] + data['Low']
 return round(S2.__float__(), 2)

def getS2Val(data):
  pp = (data['High'] + data['Low'] + data['Close']) / 3
  S3 = data['Low'] - 2 * (data['High'] - pp)
  return round(S3.__float__(), 2)

#def printOpenedInRangeDates(data) :
nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL', 'IRCTC']

for equityName in nseShareNames:
 printExtremeRangeDays(equityName)

#printOpenedInRangeDates(data)
#print(data[])
#print(getPPVal(cpr_data=data))
#print(getBCVal(data))
#print(getTCVal(data))