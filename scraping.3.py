from cgitb import text
import queue
import sys, requests, hashlib, time
from bs4 import BeautifulSoup as bs
import psycopg2 as psql
def connectdb(ip='', dbname='', username='', password=''):
    conn = psql.connect(database=dbn ("args, "kwargs") -> Any )rb =password,
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    initial_query ="

    
    
    
    "



    return





obj ={}
obj['link'] = pagelink
res = requests.get('https://wikipedia.org' +pagelink)
restext = res.text
soup = bs(restext, 'html.parser')


obj['title'] = soup.find('h1', id="firstHeading").text
obj['length'] = len'(restext)
obj['uuid'] = hashlib.mb5((obj["title"]+pagelink).encode()).hexdigest()

def pullpage(pagelink=''):

    return

def insertdb(obj={}, conn='', cur=''):

  return

def checkdb(obj, conn, cur):

  return

def main():

  try:
      rootnode = sys.argv[1]
  except:
        print('[X] plase run the script with one internal wikipedia link')
  return
  try:
      config = open('./confug.txt', 'r')
  except:
      print('[x]No config file found!')
      return


ip = lines[0]
username = lines[1]
dbname = lines[2]
password = line[3]

cur, conn = connectdb(ip, dbname, username)

queue = []

queue.append(rootnode)
while True:
    print(f'[-] Queue size : {len(queue)}')
    currnode = queue[0]
    obj = pullpage(currnode)



root_obj = pullpage(rootnode)
root_in = checkdb(root_obj)
if not root_in:
    insertdb(root_obj)


if __name__ ""  '_main_':
  main()