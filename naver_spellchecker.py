import requests as req
import re
import json

def naver_spellchecker(q):
    url = 'https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?'
    params = {
        '_callback': 'window.__jindo2_callback._spellingCheck_0',
        'q': q
    }
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://news.naver.com/main/home.nhn',  # 뉴스홈
    }
    response = req.get(url=url, params=params, headers=request_headers).text

    # json 형식으로 만들기
    response = response.replace('window.__jindo2_callback._spellingCheck_0(', '')
    response = response.replace(');', '')

    # json 화 json.dumps() 의 반대
    response_dict = json.loads(response)

    result = response_dict['message']['result']['html']
    result =re.sub(r'<\/?.*?>','',result)

    print('수정 후:'+result)

if __name__=='__main__':
    contents=input()
    print('수정 전'+contents)
    naver_spellchecker(contents)
