import nsepy as nse

q=nse.get_quote('')
print(q['data'][0]['lastPrice'])