import upstox
from upstox_api.api import *


s = Session ('b6612aa6-11cc-47f5-a7a3-59c1c071f3f1')
s.set_redirect_uri ('https://pro.upstox.com/trading')
s.set_api_secret('your_api_secret')
