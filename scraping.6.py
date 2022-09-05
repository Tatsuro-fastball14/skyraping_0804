import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

# r = requests.get('https://shigira.com/hotel/shigira/guestrooms/suite-villa-sunrise', headers=headers)

r = requests.get('https://www.apahotel.com/hotel/syutoken/tokyo/shibuya-dougenzakaue/',headers=headers)
print(r.text)
print('---------------')
soup = BeautifulSoup(r.content, 'html.parser')
h1 = soup.find('title')
print('タイトル',h1)
