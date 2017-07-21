from crawling import *

def csv_mail():
    url ='http://comic.naver.com/webtoon/weekday.nhn'
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://news.naver.com/main/home.nhn',  # 뉴스홈
    }

    html =req.get(url,headers=request_headers).text
    soup = bfs(html,'html.parser')

    webtoon_list = []
    for tag in soup.select('div.thumb a img[src*=http://thumb]'):
        comic = str(tag['title'])
        webtoon_list.append(comic)

    total_list = []

    for idx, name in enumerate(webtoon_list, 1):
        if idx % 6 == 1:
            if idx > 6:
                total_list.append(list1)
            list1 = []
        list1.append(webtoon_list[idx - 1])

    with open('naver_webtoon.csv', 'wt', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(total_list)


    password = getpass.getpass('password:')

    message = EmailMessage()

    message['Subject'] = '네이버 웹툰 업데이트 리스트'
    message['From'] = 'qoentlr37@naver.com'
    message['To'] = 'qoentlr37@gmail.com'

    message.set_content('네이버 웹툰 list csv 파일로 보내기')

    message.add_alternative('''
        <h1>파이썬 자동화-이미지 첨부 메일 보내기</h1>

        <p>이 프로젝트의 시작은 Facebook의 대나무숲에서 시작됐습니다.
        기말 고사 일주일 전, 페이스북 대나무 숲에서 많은 친구들이 이성친구가 없어서 외로움을 호소하는 것을 발견했고,
        작은 도움이라도 주고 싶다는 생각을 했습니다. 취업 문제, 등록금 문제등으로 많은 어려움을 겪는 20대 들에게 연애를 위해
        많은 시간을 할애하는 일은 쉽지 않습니다. 더욱이 시험을 앞두고 심신으로 지친 친구들에게 시험이 끝나면 소개팅이 기다리고 있다는 작은 설렘을 전달하고 싶었습니다.
        당시에 부족한 실력이지만 Django라는 프레임워크를 막 공부하기 시작했기 때문에 간단한 프로젝트 통해서 공부도하고,
        그 친구들에게 작은 도움이라도 주고 싶어 [취미]와 [라이프 스타일], [연애 스타일]을 기반으로 한 매칭 프로젝트인 '데이터 소개팅'을 기획하게 됐습니다.</p>
        ''')

    filepath ='naver_webtoon.csv'
    with open('naver_webtoon.csv','rb') as f:
        filename =os.path.basename(filepath)
        img_data = f.read()
        part = MIMEApplication(img_data, name=filename)


            # Content-Disposition 헤더 추가 시에
        part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % filename)

    message.attach(part)

    with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
        server.ehlo()
        server.login('qoentlr37', 'Erunc837!!')
        server.send_message(message)


    print('{}님이 {}님에게 이메일을 보냈습니다~!'.format(message['From'], message['To']))


if __name__ == '__main__':
    print('웹툰 제목들이 담긴 csv파일을 메일로 보내드리겠습니다.')
    csv_mail()
