from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from functions import *

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

login(browser, 'hzoltan@gmail.com', 'Jelszo123')
navigate_to_settings(browser)
change_profile_pic(browser, 'https://i.pinimg.com/474x/7c/4d/15/7c4d1533480bb4c5911d95699fef5186.jpg')

update_msg = browser.find_element_by_xpath('//div[@class="swal-title"]')
assert update_msg.text == 'Update successful!'
ok_btn = browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
ok_btn.click()

browser.quit()

