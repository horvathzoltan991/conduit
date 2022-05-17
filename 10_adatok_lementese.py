from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = 'http://localhost:1667/'

browser.get(URL)

tags = browser.find_elements_by_xpath('//a[@class="tag-pill tag-default"]')
with open('tags.txt', 'w') as f:
    for tag in tags:
        f.write(tag.text + ', ')

with open('tags.txt', 'r') as f:
    txt_tags = f.read().split(', ')
    for i, tag in enumerate(tags):
        assert tag.text == txt_tags[i]
