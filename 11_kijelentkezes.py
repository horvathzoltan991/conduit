from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')
logout(browser)

sign_in_btn = browser.find_element_by_xpath('//a[@href="#/login"]')
assert sign_in_btn.is_displayed()

browser.quit()