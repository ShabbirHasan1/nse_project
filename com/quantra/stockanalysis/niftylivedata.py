import nsepy as nse

q=nse.get_quote('HDFCBANK')
print(q['data'][0]['lastPrice'])
