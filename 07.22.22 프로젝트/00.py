from http.client import PAYMENT_REQUIRED
from urllib import response
import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL) # URL ?(종목과 원화)정보를 response에 넣는다. 

data = response.json() #요청한 json 정보를 data에 넣는다. 
print(data.get('data').get('closing_price')) 
# data 딕셔너리에 key로 접근한다. 
