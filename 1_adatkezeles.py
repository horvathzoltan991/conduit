from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

accept_cookie(browser)

accept_cookie_btn_list = browser.find_elements_by_xpath(
    '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
assert len(accept_cookie_btn_list) == 0

browser.quit()
