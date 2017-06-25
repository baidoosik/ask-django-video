import requests
from bs4 import BeautifulSoup as bs


def askdjango_level1(url):
    html = requests.get(url).text
    soup =bs(html,'html.parser')

    for tag in soup.select('#course_list > .course > a'):
        print(tag.text,tag['href'])

if __name__ == '__main__' :
    askdjango_level1('https://askdjango.github.io/lv1/')


