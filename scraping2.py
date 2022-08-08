import requests as req
print(f'[-] Requets library is installed!')
import time
from bs4 import BeautifulSoup as soup
import psycopg2 as psql

DBNAME = 'test'
DBNAME = 'testdb'
DBNAME = 'password'
DBNAME = '10.0.0.8'
def main():





  base_url ='https://finance/yahoo.com/quote/'
  cur = conn.cursor()


  stocks =['AAPL','MSFT','GME','GOOG','T','chickentendies']

  res = req.get(base_url)
