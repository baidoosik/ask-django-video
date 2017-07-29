from crawling import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def naver_mail():
    password = getpass.getpass('password:')
    mail_list=[]
    mail_str=''
    try:
        driver = webdriver.Chrome('/Users/doosikbai/chromedriver')

        driver.get('http://naver.com')
        time.sleep(2)

        tag_id = driver.find_element_by_name('id')
        tag_id.send_keys('qoentlr37')

        tag_pw = driver.find_element_by_name('pw')
        tag_pw.send_keys(password)

        tag_pw.submit()

        driver.find_elements_by_css_selector('a.btn')[0].click()
        driver.find_elements_by_css_selector('a.btn_close')[0].click()
        # 메일 리스트로 이
        driver.get('https://m.mail.naver.com')

        html = driver.page_source
        result = re.search(r'var oFolderList = (.*?)\"OK\"}', html, re.S)

        result = result[0].replace('var oFolderList = ', '')

        response_dict = json.loads(result)
        print(response_dict['mailData'][0]['from']['name'], response_dict['mailData'][0]['subject'])

        for tag in response_dict['mailData']:
            mail_list.append(tag['from']['name']+tag['subject'])


    finally:
        driver.close()

    for content in mail_list:
        mail_str = mail_str +content+'\n'+'\n'

    message = EmailMessage()
    message['Subject'] = '네이버 메일 리스트'
    message['From'] = 'qoentlr37@naver.com'
    message['To'] = 'qoentlr37@gmail.com'

    message.set_content(mail_str)

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('qoentlr37', password)
        server.send_message(message)

    print('{}님이 {}님에게 이메일을 보냈습니다~!'.format(message['From'], message['To']))



if __name__=='__main__':
    print('두식님의 메일을 모아오겠습니다.')
    naver_mail()






