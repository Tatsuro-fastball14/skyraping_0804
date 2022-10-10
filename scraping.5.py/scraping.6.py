#Chromiumとseleniumをインストール

!apt-get update

!apt install chromium-chromedriver

!cp /usr/lib/chromium-browser/chromedriver/usr/bin

!pip install selenium


#ライブラリをインポート

from selenium import webdriver

import time

options = webdriver.ChromeOptions()

options.add_argument('--headless')

options.add_argument('--no-sandbox')

options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver',options=options)

driver.implicitly_wait(10)


print("サイトにアクセス開始")

driver.get("https://www.google.com/")

time.sleep(3)

print("サイトのタイトル：", driver.title)

print("\nお疲れさまです。\n処理が完了しました。")



driver.get("https://go-theshigira.reservation.jp/ja/hotels/shigira/rooms?checkin_date=20221022&checkout_date=20221023&adults=2&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0")


print(driver.page_source)