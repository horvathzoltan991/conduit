import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def accept_cookies(browser):
    accept_cookie_btn = browser.find_element_by_xpath(
        '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
    accept_cookie_btn.click()
    time.sleep(1)


def registration(browser, username, email, password):
    sign_up_nav_btn = browser.find_element_by_xpath('//a[@href="#/register"]')
    sign_up_nav_btn.click()
    name_input = browser.find_element_by_xpath('//input[@type="text" and @placeholder="Username"]')
    name_input.send_keys(username)
    email_input = browser.find_element_by_xpath('//input[@type="text" and @placeholder="Email"]')
    email_input.send_keys(email)
    password_input = browser.find_element_by_xpath('//input[@type="password" and @placeholder="Password"]')
    password_input.send_keys(password)
    sign_up_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_up_btn.click()


def login(browser, email, password):
    sign_in_nav_btn = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
    sign_in_nav_btn.click()
    email_input = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
    email_input.send_keys(email)
    password_input = browser.find_element_by_xpath('//input[@type="password"]')
    password_input.send_keys(password)
    sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()


def logout(browser):
    log_out_btn = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, '//ul/li[5]/a')))
    log_out_btn.click()


def publish_article(browser, title, summary, text, tag):
    new_article_btn = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))
    new_article_btn.click()
    article_title = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//fieldset/input[@class="form-control form-control-lg"]')))
    article_title.send_keys(title)
    article_summary = browser.find_element_by_xpath('//fieldset/input[@class="form-control"]')
    article_summary.send_keys(summary)
    article_text = browser.find_element_by_xpath('//textarea')
    article_text.send_keys(text)
    article_tag = browser.find_element_by_xpath('//input[@placeholder="Enter tags"]')
    article_tag.send_keys(tag)
    publish_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg pull-xs-right btn-primary"]')
    publish_btn.click()


def add_comment(browser, comment):
    time.sleep(1)
    first_post = browser.find_elements_by_xpath('//h1')[1]
    first_post.click()
    comment_textarea = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
    comment_textarea.send_keys(comment)
    post_btn = browser.find_element_by_xpath('//button[@class="btn btn-sm btn-primary"]')
    post_btn.click()


def navigate_to_settings(browser):
    settings_btn = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//a[@href="#/settings"]')))
    settings_btn.click()


def change_profile_pic(browser, url):
    picture_link_input = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//input[@placeholder="URL of profile picture"]')))
    picture_link_input.clear()
    picture_link_input.send_keys(url)
    update_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    update_btn.click()


def delete_comment(browser):
    delete_btn = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
    delete_btn.click()
    time.sleep(1)
