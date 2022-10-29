import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary 
import requests
from bs4 import BeautifulSoup

cmd = 'pip install --upgrade chromedriver_binary' 
res = subprocess.call(cmd, shell=True)
url = "https://go-theshigira.reservation.jp/ja/hotels/santamonica/plans?checkin_date=20221023&checkout_date=20221024&adults=2&child1=0&child2=0&child3=0&child4=0&child5=0&children=0&rooms=1&dayuseFlg=0"
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'performance': 'ALL' }
def new_func(d):
    return webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)
   

driver = new_func(d)
driver.set_window_size('1200','1000')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(driver.page_source)
li=soup.find_all('li', class_="u-flex1 u-flex-center")
print(li)


