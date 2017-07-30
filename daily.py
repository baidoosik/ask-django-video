import json
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from crawling import Crawling_Tool


def daily_info():
    tool = Crawling_Tool()
    mail_str =''

    with open("envs.json") as f:
        envs = json.loads(f.read())

    admin_password = envs['admin_password']
    google_password = envs['google_password']
    try:
        admin_url=envs['admin_url']

        driver = webdriver.Chrome('/Users/doosikbai/chromedriver')
        driver.get(admin_url)

        login_id = driver.find_element_by_css_selector('input#id_username')
        login_id.send_keys('doosik')

        login_pw = driver.find_element_by_css_selector('input#id_password')
        login_pw.send_keys(admin_password)

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

    finally:
        driver.close()


    try:

        driver = webdriver.Chrome('/Users/doosikbai/chromedriver')

        driver.get('https://play.google.com/apps/publish/')

        google_id = driver.find_element_by_id('identifierId')
        google_id.send_keys('qoentlr37')

        google_next = driver.find_element_by_css_selector('content.CwaK9')

        google_next.click()

        time.sleep(2)

        google_pw = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
        google_pw.send_keys(google_password)

        google_pw.submit()

        google_next2 = driver.find_element_by_css_selector('#passwordNext > content > span')
        google_next2.click()

        time.sleep(10)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        print('화장실 어플 다운로드'+soup.select('td > div > a > span')[0].text)
        mail_str ='\n'+ mail_str +'화장실 물소리 어플 다운로드'+ soup.select('td > div > a > span')[0].text +'\n'

    finally:
        driver.close()

    Crawling_Tool.get_mail(tool, mail_str=mail_str)

if __name__ == '__main__':
    print('Daily 데이터를 메일로 보내드리겠습니다.')
    daily_info()




