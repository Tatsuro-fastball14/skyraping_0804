#アパホテルのサイトをスクレイピングするコード

import requests
import pickle
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

with open('./before_article.pickle', 'rb')as f:
    before_new_article =pickle.load(f)

html =requests.get(r)
soup =BeautifulSoup(html.content, "html.parser")

new_article = str(soup.find(class_="entry-card-wrap").get("title"))
with open('./before_article.pickle', 'wb') as f:
    pickle.dump(before_article.pickle, f)

if new_article != before_new_article:
    print('新着あり')