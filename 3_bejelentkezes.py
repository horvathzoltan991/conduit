from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

sign_in_nav_btn = browser.find_element_by_xpath('//a[@href="#/login"]')
sign_in_nav_btn.click()

email_input = browser.find_element_by_xpath('//input[@type="text"]')
email_input.send_keys('hzoltan@gmail.com')

password_input = browser.find_element_by_xpath('//input[@type="password"]')
password_input.send_keys('Jelszo123')

sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_in_btn.click()

time.sleep(1)

profile_btn = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
assert profile_btn.text == 'hzoltan'
browser.quit()
