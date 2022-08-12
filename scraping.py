from email.mime import base
import requests
from bs4 import BeautifulSoup
import time

import sys
print('pythonのバージョンは' + str(sys.version) + 'です')

def main():
  base_url = 'https://finance.yahoo.com/quote/'

  stocks =['AAPL','MSFT','GME','GOOG','T']

  res = requests.get(base_url)
  print(f'[-] Status code: {res.status_code}')

  for ticker in stocks:
      stockpage = requests.get(base_url+ticker)
      print(f'[-] Status code: {stockpage.status_code}')
      if stockpage.status_code ==200:

        source = stockpage.text
        parsedpage = BeautifulSoup(source, 'html.parser')
        try:
          price = parsedpage.find('fin-streamer', class_= 'Fw(b) Fz(36px) Mb(-4px) D(ib)')
          print(f'[-] Ticker {ticker} has price {price.text}!')
          print(f'/t[-] {base_url+ticker}')
          try:
            try:
              delta = parsedpage.find('span', attrs={'data-reactid:50'}).text
            except:
              pass
          except:
            pass
        except:
          pass
      else:
        print(f'[x] Request to page {base_url+ticker} failed, status code: {stockpage.status_code}')
        time.sleep(1)
main()