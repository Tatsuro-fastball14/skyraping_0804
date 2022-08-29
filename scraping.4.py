#アパホテルのサイトをスクレイピングするコード

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

r = requests.get('https://asia.creativecdn.com/tags?type=iframe&id=pr_i2T7Cnz3c0D6sTUEk6m9', headers=headers)

print(r.text)
print('---------------')
soup = BeautifulSoup(r.text)
h1 = soup.find('h1')
print('タイトル',h1)

