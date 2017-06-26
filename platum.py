import requests as req
from bs4 import BeautifulSoup as bfs

def platum_interview():
    url ='http://platum.kr/'

    html = req.get(url=url).text
    soup = bfs(html,'html.parser')

    result = soup.select('.inner_wrapper .post_wrapper h5 a[href*="platum"]')

    for idx,tag in enumerate(result,1):
        print(idx,tag.text)


if __name__ == '__main__' :
    platum_interview()
