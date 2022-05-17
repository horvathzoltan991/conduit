from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')

ipsum_tag = browser.find_element_by_xpath('//div[@class="sidebar"]/div[@class="tag-list"]/a[text()="ipsum"]')
ipsum_tag.click()
time.sleep(1)
articles = browser.find_elements_by_xpath('//a[@class="preview-link"]/h1')
assert len(articles) > 0

browser.quit()

