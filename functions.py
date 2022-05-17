import time

def login(browser, email, password):
    sign_in_nav_btn = browser.find_element_by_xpath('//a[@href="#/login"]')
    sign_in_nav_btn.click()
    email_input = browser.find_element_by_xpath('//input[@type="text"]')
    email_input.send_keys(email)
    password_input = browser.find_element_by_xpath('//input[@type="password"]')
    password_input.send_keys(password)
    sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
    time.sleep(2)
