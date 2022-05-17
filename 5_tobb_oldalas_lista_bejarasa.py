from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')

page_links = browser.find_elements_by_xpath('//a[@class="page-link"]')

for page_link in page_links:
    page_link.click()

assert int(page_links[-1].text) == len(page_links)

browser.quit()
