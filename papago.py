from crawling import *

class Papago_Ko_en():

    def info_setting(self):
        self.url = 'http://labspace.naver.com/api/n2mt/translate'

        self.request_headers = {
            'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
            'Referer': 'http://labspace.naver.com/nmt/',
            'x-naver-client-id': 'labspace'
        }

    def data_setting(self):
        self.data = {'source': 'ko',
                'target': 'en',
                'text': ''}

    def __call__(self):
        self.info_setting()
        self.data_setting()
        print('번역하기 원하는 내용을 적어주세요!')
        q=input()
        self.data['text']=q
        html = req.post(url=self.url, data=self.data, headers=self.request_headers).text
        response = json.loads(html)
        dict = response['message']['result']['translatedText']
        print('파파고 변역 전:',q)
        print('파파고 번역 결과:',dict)


class Papago_En_ko(Papago_Ko_en):

    def data_setting(self):
        self.data = {'source': 'en',
                'target': 'ko',
                'text': ''}


class Papago_Ko_ch(Papago_Ko_en):
    def data_setting(self):
        self.data = {'source': 'ko',
                     'target': 'zh-CN',
                     'text': ''}

if __name__=='__main__':
    print('원하는 번역의 번호를 선택하고 번호를 입력해주세요.')
    print('한글 -> 영어:1')
    print('영어 -> 한글:2')
    print('한글 -> 중국어:3')

    opt=input()

    if opt=='1':
        korea_papago = Papago_Ko_en()
        korea_papago()
    elif opt == '2':
        english_papago = Papago_En_ko()
        english_papago()
    elif opt == '3':
        china_papago = Papago_Ko_ch()
        china_papago()
    else:
        print('번호를 잘 못 누르셨습니다 1~3 을 선택해주세요!')
        exit()


