from crawling import *
import asyncio
from slacker import Slacker
import websockets

async def bot():
    token = getpass.getpass('token을 입려해 주세요.')
    slacker = Slacker(token)

    response = slacker.rtm.start()
    meta = response.body

    ws = await websockets.connect(meta['url'])

    try:
        while True:
            response =json.loads(await ws.recv())

            if 'message' == response.get('type',None):
                if 'channel' in response:
                    await ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': 'Echo:' + response['text'],
                    }))

            time.sleep(1)

    finally:
        await ws.close()

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot())

    except KeyboardInterrupt:
        print('봇 서버를 종료시키겠습니다.')

    finally:
        loop.close()