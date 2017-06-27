import requests as req
from bs4 import BeautifulSoup as bfs
import re

def reddit_crawling():

    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'), 'Referer': 'http://news.naver.com/main/home.nhn', # 뉴스홈
    }

    html =req.get(url='https://www.reddit.com/',headers=request_headers).text

    soup = bfs(html,'html.parser')

    for idx, tag in enumerate(soup.select('#siteTable p.title a'), 1):
        print(idx, tag.text, 'https://www.reddit.com/' + tag['href'])


if __name__=='__main__':
    reddit_crawling()

