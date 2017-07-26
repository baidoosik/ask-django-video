from crawling import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def naver_mail():
    password = getpass('password:')

    try:
        driver = webdriver.Chrome('/Users/doosikbai/chromedriver')

        driver.get('httmp://naver.com')
        time.sleep(2)

        tag_id = driver.find_element_by_name('id')

        tag_id.send_keys('qoentlr37')

        tag_pw = driver.find_element_by_name('pw')

        tag_pw.send_keys(password)

        tag_pw.submit()

        driver.get('')
