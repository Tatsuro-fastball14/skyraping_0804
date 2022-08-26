#アパホテルのサイトをスクレイピングするコード

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

r = requests.get('https://www.apahotel.com/hotel/syutoken/chiba/keiseinarita-ekimae/', headers=headers)

print(r.text)
print('---------------')
soup = BeautifulSoup(r.text)
h1 = soup.find('h1')
print('タイトル',h1)

