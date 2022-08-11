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

  conn = psql.connect(database=DBNAME, user=DBUSER, password=DBPASS, host=DBHOST, pory=5432)
  cur = conn.cursor()


  initial_query = """
  CREATE TABLE IF NOT EXISTS stock_data
  (uuid TEXT NOT NULL, timestamp TEXT NOT NULL, tocker TEXT NOT NULl)
  """

  cur.execute(initial_query)
  conn.commit()






  base_url ='https://finance/yahoo.com/quote/'
  cur = conn.cursor()


  stocks =['AAPL','MSFT','GME','GOOG','T','chickentendies']

  res = req.get(base_url)
