from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from functions import *
import csv
import time


class TestConduit(object):
    def setup(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        url = 'http://localhost:1667/'
        self.browser.get(url)

    def teardown(self):
        self.browser.quit()

    def test_accept_cookies(self):
        accept_cookies(self.browser)
        accept_cookie_btn_list = self.browser.find_elements_by_xpath(
            '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
        assert len(accept_cookie_btn_list) == 0

    def test_sign_up(self):
        sign_up_nav_btn = self.browser.find_element_by_xpath('//a[@href="#/register"]')
        sign_up_nav_btn.click()
        sign_up_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_btn.click()
        time.sleep(1)
        error_msg = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
        error_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        assert error_msg.text == 'Registration failed!'
        assert error_reason.text == 'Username field required.'

    def test_login(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        profile_btn = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
        assert profile_btn.text == 'hzoltan'

    def test_display_list(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        ipsum_tag = self.browser.find_element_by_xpath(
            '//div[@class="sidebar"]/div[@class="tag-list"]/a[text()="ipsum"]')
        ipsum_tag.click()
        time.sleep(1)
        articles = self.browser.find_elements_by_xpath('//a[@class="preview-link"]/h1')
        assert len(articles) > 0

    def test_pagination(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        page_links = self.browser.find_elements_by_xpath('//a[@class="page-link"]')
        for page_link in page_links:
            page_link.click()
            time.sleep(1)
        assert int(page_links[-1].text) == len(page_links)

    def test_create_new_article(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        publish_article(self.browser, 'Title', 'Summary', 'Text', 'Tag')
        published_article_title = self.browser.find_element_by_xpath('//div/h1')
        assert published_article_title.text == 'Title'

    def test_import_data_from_file(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        with open('Test_Conduit/article.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                publish_article(self.browser, row[0], row[1], row[2], row[3])
        published_article_title = self.browser.find_element_by_xpath('//div/h1')
        assert published_article_title.text == 'CSV Title'

    def test_update_profile_pic(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        navigate_to_settings(self.browser)
        change_profile_pic(self.browser, 'https://i.pinimg.com/474x/7c/4d/15/7c4d1533480bb4c5911d95699fef5186.jpg')
        update_msg = self.browser.find_element_by_xpath('//div[@class="swal-title"]')
        assert update_msg.text == 'Update successful!'

    def test_delete_comment(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        add_comment(self.browser, 'This is a comment!')
        delete_comment(self.browser)
        comments = self.browser.find_elements_by_xpath('//div[@class="card"]')
        assert len(comments) == 0

    def test_save_data_to_file(self):
        tags = self.browser.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
        with open('Test_Conduit/tags.txt', 'w') as f:
            for tag in tags:
                f.write(tag.text + ', ')
        with open('Test_Conduit/tags.txt', 'r') as f:
            txt_tags = f.read().split(', ')
            for i, tag in enumerate(tags):
                assert tag.text == txt_tags[i]

    def test_logout(self):
        login(self.browser, 'hzoltan@gmail.com', 'Jelszo123')
        logout(self.browser)
        sign_in_btn = self.browser.find_element_by_xpath('//a[@href="#/login"]')
        assert sign_in_btn.is_displayed()
