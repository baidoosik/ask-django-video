from crawling import *

def askdjango_lv123():
    url1 = 'https://askdjango.github.io/lv1/'
    url2= 'https://askdjango.github.io/lv2/data.json'
    url3 ='https://askdjango.github.io/lv3/'


    html = req.get(url1).text
    soup1 = bfs(html,'html.parser')

    print('크롤링 level 1!')

    for idx,tag in enumerate(soup1.select('ul li a'),1):
        print(idx,tag.text,tag['href'])

    print('크롤링 level 2!')
    html2 = req.get(url2).text
    json_dict = json.loads(html2)

    for tag in json_dict:
        print(tag['name'],tag['url'])


    print('크롤링 level 3!')

    html3 = req.get(url3).text
    soup3 = bfs(html3,'html.parser')

    matched=re.search(r'var courses = (.*?);',html3,re.S)

    print(matched.group(1))


if __name__ =='__main__':
    print('program is now operating!')
    askdjango_lv123()