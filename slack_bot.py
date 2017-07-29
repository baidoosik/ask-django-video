from crawling import *
from slacker import Slacker
import websocket

token = getpass.getpass('token:')

slack = Slacker(token)

response = slack.rtm.start()
meta = response.body

ws = websocket.create_connection(meta['url'])

try:
    while True:
        resp = json.loads(ws.recv())
        print(resp)
        if "message" == resp.get("type",None):
            if 'channel' in resp:
                ws.send(json.dumps({
                        'channel':resp['channel'],
                        'type': 'message',
                        'text':'ECHO'+resp['text'],
                    }))
    time.sleep(1)

except KeyboardInterrupt:
    print('봇 서버가 종료됩니다')

finally:
    ws.close()