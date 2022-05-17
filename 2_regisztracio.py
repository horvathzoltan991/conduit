from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

sign_up_nav_btn = browser.find_element_by_xpath('//a[@href="#/register"]')
sign_up_nav_btn.click()

sign_up_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_up_btn.click()

time.sleep(1)

error_msg = browser.find_element_by_xpath('//div[@class="swal-title"]')
error_reason = browser.find_element_by_xpath('//div[@class="swal-text"]')
assert error_msg.text == 'Registration failed!'
assert error_reason.text == 'Username field required.'

browser.quit()
