import requests as req
import re
import json
from bs4 import BeautifulSoup as bfs
import time
from PIL import Image
import os
import math
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
import getpass
import csv


class Crawling_Tool:
    def request_url(url):
        html = req.get(url)
        soup = bfs(html,'html.parser')

    def get_password(self):
        return getpass.getpass('password:')

    def get_mail(self,mail_str='naver_str'):
        with open("envs.json") as f:
            envs = json.loads(f.read())
        naver_password = envs['naver_password']

        message = EmailMessage()
        message['Subject'] = '네이버 메일 리스트'
        message['From'] = 'qoentlr37@naver.com'
        message['To'] = 'qoentlr37@gmail.com'

        message.set_content(mail_str)

        with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
            server.ehlo()
            server.login('qoentlr37', naver_password)
            server.send_message(message)

        print('{}님이 {}님에게 이메일을 보냈습니다~!'.format(message['From'], message['To']))


