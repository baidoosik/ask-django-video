from crawling import *

def update_news():

    up_comic_list = []

    url = 'http://comic.naver.com/webtoon/weekday.nhn'
    headers = {
        'referer': url
    }

    html = req.get(url, headers=headers).text
    soup = bfs(html, 'html.parser')

    result = soup.select('#container #content div.thumb a')

    for tag in result:
        if tag.select('em.ico_updt'):
            img_tag = tag.find('img')
            title = img_tag['title']
            img_url = tag['href']

            img_url = 'http://comic.naver.com/'+img_url

            up_comic_list.append({
                'title': title,
                'img_url': img_url
            })

    password = getpass.getpass('password:')

    message = EmailMessage()

    message['Subject'] = '네이버 웹툰 업데이트 리스트'
    message['From'] = 'qoentlr37@naver.com'
    message['To'] = 'leejh920917@gmail.com'

    message.set_content(str(up_comic_list))

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('qoentlr37', 'Erunc837!!')
        server.send_message(message)

    print('{}님이 {}님에게 이메일을 보냈습니다~!'.format(message['From'], message['To']))

if __name__=='__main__':
    print('오늘 업데이트된 웹툰 제목과 리스트를 메일로 보내드리겠습니다.')
    update_news()