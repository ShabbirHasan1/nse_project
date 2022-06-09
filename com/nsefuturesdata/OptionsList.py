
from nsetools import Nse

nse = Nse()
print(nse.get_stock_codes())
print()
print(nse.get_quote('ZEEL'))
nse.get_quote_url
#print(nse.get_index_list())