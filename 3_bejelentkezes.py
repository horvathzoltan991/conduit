from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from functions import *
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')

profile_btn = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
assert profile_btn.text == 'hzoltan'
browser.quit()
