from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')
publish_article(browser, 'Title', 'Summary', 'Text', 'Tag')

published_article_title = browser.find_element_by_xpath('//div/h1')

assert published_article_title.text == 'Title'

browser.quit()
