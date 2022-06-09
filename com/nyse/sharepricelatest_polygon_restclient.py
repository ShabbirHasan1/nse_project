from polygon import RESTClient


def getPriceConversionRate(from_currency, to_currency):
    key = "_UB2XQ2tym7l_OEOwqjsUQdDR6bSIQysfBHhTb"
    client = RESTClient(key)

    resp = client.forex_currencies_last_quote_for_a_currency_pair(from_currency, to_currency)
    #print(type(resp))
    return resp.__getattribute__('last').__getattribute__('ask')


conversion_rate = getPriceConversionRate('EUR', 'USD')
print(type(conversion_rate))
