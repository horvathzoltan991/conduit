from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')

with open('article.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        publish_article(browser, row[0], row[1], row[2], row[3])

published_article_title = browser.find_element_by_xpath('//div/h1')
assert published_article_title.text == "CSV Title"

browser.quit()