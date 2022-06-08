from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from functions import *
from data import test_data
import csv


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        url = 'http://localhost:1667/'
        self.browser.get(url)

    def teardown(self):
        self.browser.quit()

    # TC01 - Adatkezelési nyilatkozat használata (elfogadása)
    def test_accept_cookies(self):
        accept_cookies(self.browser)
        accept_cookie_btn_list = self.browser.find_elements_by_xpath(
            '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
        assert len(accept_cookie_btn_list) == 0

    # TC02 - Regisztráció (hiányzó felhasználónévvel)
    def test_sign_up(self):
        registration(self.browser, test_data['invalid_username'], test_data['invalid_email'],
                     test_data['invalid_password'])
        error_msg = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        error_reason = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        assert error_msg.text == 'Registration failed!'
        assert error_reason.text == 'Username field required.'

    # TC03 - Bejelentkezés (helyes adatokkal)
    def test_login(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        time.sleep(10)
        profile_btn = self.browser.find_element_by_xpath('//a[@href="#/@hzoltan/" and @class="nav-link"]')
        assert profile_btn.text == 'hzoltan'

    # TC04 - Adatok listázása (tagek listázása)
    def test_display_list(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        ipsum_tag = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@class="sidebar"]/div[@class="tag-list"]/a[text()="ipsum"]')))
        ipsum_tag.click()
        time.sleep(1)
        articles = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))
        assert len(articles) > 0

    # TC05 - Több oldalas lista bejárása (bejegyzések végiglapozása)
    def test_pagination(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        page_links = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
        for page_link in page_links:
            page_link.click()
        assert int(page_links[-1].text) == len(page_links)

    # TC06 - Új adat bevitel (új bejegyzés posztolása)
    def test_create_new_article(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        publish_article(self.browser, test_data['article_title'], test_data['article_summary'],
                        test_data['article_text'],
                        test_data['article_tag'])
        published_article_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div/h1')))
        assert published_article_title.text == 'Test Title'

    # TC07 - Ismételt és sorozatos adatbevitel adatforrásból (bejegyzés adatainak beolvasása csv-ből)
    def test_import_data_from_file(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        with open('Test_Conduit/article.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                publish_article(self.browser, row[0], row[1], row[2], row[3])
        published_article_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div/h1')))
        assert published_article_title.text == 'CSV Title'

    # TC08 - Meglévő adat módosítás (profilkép megváltoztatása)
    def test_update_profile_pic(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        navigate_to_settings(self.browser)
        change_profile_pic(self.browser, 'https://i.pinimg.com/474x/7c/4d/15/7c4d1533480bb4c5911d95699fef5186.jpg')
        update_msg = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        assert update_msg.text == 'Update successful!'

    # TC09 - Adat vagy adatok törlése (komment törlése)
    def test_delete_comment(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        add_comment(self.browser, test_data['test_comment'])
        delete_comment(self.browser)
        comments = self.browser.find_elements_by_xpath('//div[@class="card"]')
        assert len(comments) == 0

    # TC10 - Adatok lementése felületről (tagek lementése txt-be)
    def test_save_data_to_file(self):
        tags = self.browser.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
        with open('Test_Conduit/tags.txt', 'w') as f:
            for tag in tags:
                f.write(tag.text + ', ')
        with open('Test_Conduit/tags.txt', 'r') as f:
            txt_tags = f.read().split(', ')
            for i, tag in enumerate(tags):
                assert tag.text == txt_tags[i]

    # TC11 - Kijelentkezés
    def test_logout(self):
        login(self.browser, test_data['valid_email'], test_data['valid_password'])
        logout(self.browser)
        sign_in_btn = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
        assert sign_in_btn.is_displayed()
