from crawling import *
from slacker import Slacker
import websocket


slack  = Slacker('xoxb-218858261169-ZuWok3iCVJyYdIFaNbIgXYZv')

response = slack.rtm.start()
meta = response.body

ws = websocket.create_connection(meta['url'])

try:
    while True:
        resp = json.loads(ws.recv())
        print(resp)
        if "message" == resp.get("type",None):
            print('어디1')
            if 'channel' in resp:
                print('어디2')
                ws.send(json.dumps({
                        'channel':resp['channel'],
                        'type': 'message',
                        'text':'ECHO'+resp['text'],
                    }))
        else:
            print('여기니')
    time.sleep(1)

except KeyboardInterrupt:
    print('봇 서버가 종료됩니다')

finally:
    ws.close()