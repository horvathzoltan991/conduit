from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

accept_btn = browser.find_element_by_xpath(
    '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
accept_btn.click()
time.sleep(1)
decline_btn_list = browser.find_elements_by_xpath(
    '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--decline"]')
assert len(decline_btn_list) == 0

browser.quit()
