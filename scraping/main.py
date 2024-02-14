from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

option = Options()
option.add_argument('--headless')


driver = webdriver.Chrome(options=option)
driver.get('https://www.oca.ac.jp/course/')
time.sleep(0.5)


html = driver.page_source.encode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

item = soup.find("div", class_="p-course_list -c2024").text
print(item)

driver.close()
driver.quit()