import time


def accept_cookie(browser):
    accept_cookie_btn = browser.find_element_by_xpath(
        '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
    accept_cookie_btn.click()
    time.sleep(2)


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


def logout(browser):
    log_out_btn = browser.find_element_by_xpath('//ul/li[5]/a')
    log_out_btn.click()
    time.sleep(2)


def publish_article(browser, title, summary, text, tag):
    new_article_btn = browser.find_element_by_xpath('//a[@href="#/editor"]')
    new_article_btn.click()
    time.sleep(2)
    article_title = browser.find_element_by_xpath('//fieldset/input[@class="form-control form-control-lg"]')
    article_title.send_keys(title)
    article_summary = browser.find_element_by_xpath('//fieldset/input[@class="form-control"]')
    article_summary.send_keys(summary)
    article_text = browser.find_element_by_xpath('//textarea')
    article_text.send_keys(text)
    article_tag = browser.find_element_by_xpath('//input[@placeholder="Enter tags"]')
    article_tag.send_keys(tag)
    publish_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg pull-xs-right btn-primary"]')
    publish_btn.click()
    time.sleep(2)


def add_comment(browser, comment):
    first_post = browser.find_elements_by_xpath('//h1')[1]
    first_post.click()
    time.sleep(2)
    comment_textarea = browser.find_element_by_xpath('//textarea[@placeholder="Write a comment..."]')
    comment_textarea.send_keys(comment)
    post_btn = browser.find_element_by_xpath('//button[@class="btn btn-sm btn-primary"]')
    post_btn.click()
    time.sleep(2)


def navigate_to_settings(browser):
    settings_btn = browser.find_element_by_xpath('//a[@href="#/settings"]')
    settings_btn.click()
    time.sleep(2)


def change_profile_pic(browser, url):
    picture_link_input = browser.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
    picture_link_input.clear()
    picture_link_input.send_keys(url)
    update_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    update_btn.click()
    time.sleep(2)


def delete_comment(browser):
    delete_btn = browser.find_element_by_xpath('//i[@class="ion-trash-a"]')
    delete_btn.click()
    time.sleep(2)
