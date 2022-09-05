#アパホテルのサイトをスクレイピングするコード

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

r = requests.get('https://shigira.com/hotel/shigira/guestrooms/suite-villa-sunrise', headers=headers)

print(r.text)
print('---------------')
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find('title')
print('タイトル',title)
soup.find_all('div',"class=t-shigiraGuestroomsDetail__roomPlanArea")
