from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')
add_comment(browser, 'This is a comment!')
delete_comment(browser)

comments = browser.find_elements_by_xpath('//div[@class="card"]')

assert len(comments) == 0

browser.quit()

