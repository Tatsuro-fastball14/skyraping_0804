from email.mime import base


def main():
  base_url = 'https://finance.yahoo.com/quote/'

  stocks =['AAPL','MSFT','GME','GOOG','T']

  res = req.get(base_url)


  print(f'[-] Status code: {res.status_code}')

  for ticker in stocks:
      stockpage = req.get(base_usl+ticker)
      print(f'[-] Status code: {stockpage.status_code}')
      if stockpage.status_code ==200:

        source = stockpage.text
        parsedpage = soup(source, 'html.parser')
        try:
          price = parsedpage.find('span', class = 'Trdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
          print(f'[-] Ticker {ticker} has price {price}!')
          print(f'/t[-] {base_url+ticker}')


          try:
            try:
                delta = parsedpage.find('span', attrs={'data-reactid:50'}).text




      else:

        print(f'[x] Request to page {base_url+ticker} failed, status code: {stockpage.status_code}')
        time.sleep(1)



