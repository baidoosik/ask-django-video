import json
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from crawling import Crawling_Tool


def daily_info():
    tool = Crawling_Tool()
    password = Crawling_Tool.get_password(tool)
    mail_str =''

    with open("envs.json") as f:
        envs = json.loads(f.read())

    try:
        admin_url=envs['admin_url']

        driver = webdriver.Chrome('/Users/doosikbai/chromedriver')
        driver.get(admin_url)

        login_id = driver.find_element_by_css_selector('input#id_username')
        login_id.send_keys('doosik')

        login_pw = driver.find_element_by_css_selector('input#id_password')
        login_pw.send_keys(password)

        login_pw.submit()

        driver.get('http://www.doosikbae.com')
        html = driver.page_source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for tag in soup.select('section.tiles a'):
            driver.get('http://www.doosikbae.com' + tag['href'])
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            print(soup.select('div.inner > h2')[0].text, soup.select('h4#hit')[0].text)
            mail_str = mail_str + (soup.select('div.inner > h2')[0].text)+(soup.select('h4#hit')[0].text)+'\n'
            time.sleep(0.5)

        Crawling_Tool.get_mail(tool,mail_str=mail_str)

    finally:
        driver.close()


if __name__ == '__main__':
    print('Daily 데이터를 메일로 보내드리겠습니다.')
    daily_info()




