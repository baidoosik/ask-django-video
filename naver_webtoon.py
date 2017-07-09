from crawling import *

def naver_webtoon(url):
    ep_headers = {
        'referer': 'http://comic.naver.com/webtoon/'
    }
    html = req.get(url, headers=ep_headers).text
    soup = bfs(html, 'html.parser')

    webtoon_name = ''.join(soup.select('div.detail h2')[0].text.split())

    ep_name = soup.select('.tit_area h3')[0].text

    result = []
    n_result = []
    file_list = []
    max_width, max_height = 0, 0
    for tag in soup.select('#comic_view_area img'):
        try:
            print(tag['src'])
            result.append(tag['src'])
        except KeyError:
            print('필요한 자료 크롤링 완료')
            break

    for img_url in result:
        print(img_url)
        if re.match(r'^http.*$', img_url):
            n_result.append(img_url)

    for img_url in n_result:
        img = req.get(img_url, headers=ep_headers).content
        img_name = os.path.basename(img_url)
        img_path = os.path.join(webtoon_name, ep_name, img_name)

        dir_path = os.path.dirname(img_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if os.path.exists(img_path):
            pass
        else:
            with open(img_path, 'wb') as f:
                f.write(img)
        file_list.append(img_path)
    for img_url in file_list:
        with Image.open(img_url) as im:
            if max_width < im.width:
                max_width = im.width

            max_height = max_height + im.height

    size = (max_width, max_height)
    white = (255, 255, 255)
    now =math.ceil(time.time())
    with Image.new('RGB', size, white) as canvas:
        height = 0
        for filename in file_list:
            with Image.open(filename) as im:
                canvas.paste(im, box=(0, height))
                height = height + im.height
        canvas.save('{}.png'.format(now))


if __name__ =='__main__':
    print('원하시는 웹툰의 url을 입력해 주세요!')
    req_url=input()
    print('으아아아 ~~요청하신 웹툰을 한 사진으로 만들어볼게요!!')
    naver_webtoon(req_url)