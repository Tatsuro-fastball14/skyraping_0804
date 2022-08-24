#アパホテルのサイトをスクレイピングするコード

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

r = requests.get('https://www.apahotel.com/', headers=headers)

print(r.text)
print('---------------')
soup = BeautifulSoup(r.text)
h1 = soup.find('h1')
print('タイトル',h1)
htmlタグ
