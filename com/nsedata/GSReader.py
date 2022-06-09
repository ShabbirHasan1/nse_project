import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('rational-cat-342318-e299ab48930a.json', scope)
client = gspread.authorize(creds)

#sheet = client.open('SharesInfo').sheet1
#purchasedShares = sheet.get_all_records()

least_share_price_sheet = client.open('SharesInfo').get_worksheet(0)
#share_data_records = least_share_price_sheet.get_all_records()

#sep_month_data_sheet = client.open('PurchasedShares').get_worksheet(2)
#future_data_sheet = client.open('PurchasedShares').get_worksheet(3)

#equity_monthly_data_sheet = client.open('PurchasedShares').get_worksheet(2)

def updateShareData(share_data):
    #equity_monthly_data_sheet.append_rows(share_data)
    least_share_price_sheet.append_rows(share_data)

'''
def updateSepMonthData(sep_equity_data):
    sep_month_data_sheet.append_rows(sep_equity_data)


def updateFutureData(nse_future_info_list):
    future_data_sheet.append_rows(nse_future_info_list)


def getSharesExpectedPrice() :
    share_data = dict()
    for share_info in purchasedShares:
        share_name = share_info.get('ShareName')
        exp_price = share_info.get('Expected Sell Amount')
        share_data[share_name] = exp_price

    return share_data


def get_november_future_low_price() :
    future_data = dict()
    future_data_low_vals = future_data_sheet.get_all_records()
    for future_info in future_data_low_vals:
        future_name = future_info.get('Future Name')
        lease_price = future_info.get('Least Price')
        future_data[future_name] = lease_price

    return future_data


def getSharesPurchasedPrice() :
    share_data = dict()
    for share_info in purchasedShares:
        share_name = share_info.get('ShareName')
        purchased_price = share_info.get('Purchase Price')
        share_data[share_name] = purchased_price

    return share_data


def getSharesLeastPriceInfo() :
    share_least_price_dict = dict()
    for share_info in share_data_records:
        share_name = share_info.get('ShareName')
        least_price = share_info.get('LeastPrice')
        share_least_price_dict[share_name] = least_price
    return share_least_price_dict

def getSharesReducedPercentInfo() :
    share_reduced_percent_dict = dict()
    for share_info in share_data_records:
        share_name = share_info.get('ShareName')
        reduced_percent = share_info.get('Percent Change')
        share_reduced_percent_dict[share_name] = reduced_percent
    return share_reduced_percent_dict'''
