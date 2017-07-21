from crawling import *

def startup_news():

    day_startup_list =[]

    #platum 최신 기사 모음
    platum_url = 'http://platum.kr/entrepreneur'
    platum_html = req.get(platum_url).text
    platum_soup = bfs(platum_html,'html.parser')

    day_startup_list.append('platum 기사 모음'+platum_url)

    for tag in platum_soup.select('h5 a'):
        day_startup_list.append(tag['title'] + ' ' + tag['href'])

    # 창조경제타운 지원사업

    kstartup_url = 'https://www.k-startup.go.kr/main.do'
    day_startup_list.append('창조경제타운 - 지원사업정보'+kstartup_url)
    kstartup_html = req.get(kstartup_url).text

    kstartup_soup = bfs(kstartup_html, 'html.parser')

    startup_str=''


    for tag in kstartup_soup.select('div#divTab01 > li > a'):
        day_startup_list.append(tag['title'])

    for info in day_startup_list:
        startup_str=startup_str+info+'\n'
    print('스타스업 관련 기사 및 정보를 크롤링 했습니다! 좋은 하루 되세요.')

    password = getpass.getpass('password:')

    message = EmailMessage()

    message['Subject']='오늘의 스타트업 기사 및 정보 리스트'
    message['From'] = 'qoentlr37@naver.com'
    message['To'] = 'qoentlr37@gmail.com'

    message.set_content(startup_str)

    with smtplib.SMTP_SSL('smtp.naver.com',465) as server:
        server.ehlo()
        server.login('qoentlr37',password)
        server.send_message(message)

    print('{}님이 {}님에게 이메일을 보냈습니다~!'.format(message['From'], message['To']))


if __name__=='__main__':
    startup_news()
