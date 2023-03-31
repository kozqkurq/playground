from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.google.co.jp/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

ll = [x for x in soup.text.split(' ') if len(x) > 0]
for elem in ll:
    print(elem)