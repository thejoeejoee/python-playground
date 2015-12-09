import json
import http.client
from pprint import pprint
from sys import argv
from time import sleep
from urllib.parse import urlencode

from pybots_hersik.zakladni_bludiste import wave


class MyBot:
    def __init__(self, host='localhost', port='44822'):
        self.host = host
        self.port = port
        self.conn = http.client.HTTPConnection(host, port)
        self.conn.request("GET", "/")
        resp = self.conn.getresponse()
        if resp.status == 200:
            data = resp.read().decode('UTF-8')
            data = json.loads(data)
            self.bot_id = data['bot_id']
            # print(data['id'])
        else:
            print(resp.status, resp.reason)
            print()
            pprint(resp.getheaders())
            print()
            print(resp.read().decode('UTF-8'))
            raise Exception("Hru se nepodarilo zalozit")

    def getmap(self):
        self.conn.request("GET", "/game/{}".format(self.bot_id))
        resp = self.conn.getresponse()
        return json.loads(resp.read().decode('UTF-8'))['map']

    def get(self, path, **param):
        enc_param = urlencode(param)
        self.conn.request('GET', '{}?{}'.format(path, enc_param))
        resp = self.conn.getresponse()
        return json.loads(resp.read().decode('UTF-8'))

    def post(self, path, **param):
        enc_param = urlencode(param)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain, application/json"}
        self.conn.request("POST", path, enc_param, headers)
        resp = self.conn.getresponse()
        return json.loads(resp.read().decode('UTF-8'))

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    Hersik = MyBot('hroch.spseol.cz')
    data = Hersik.get('/game/{}'.format(Hersik.bot_id))
    print(Hersik.bot_id)
    labyrint = data['map']
    bool_bots = [data.get('bots')[0].get('your_bot'), data.get('bots')[-1].get('your_bot')]
    position_start = (
        data.get('bots')[bool_bots.index(True)].get('y'),
        data.get('bots')[bool_bots.index(True)].get('x')
    )
    print(position_start)
    cesta = wave(labyrint, location=data.get('bots')[0].get('orientation'), start=position_start, enemy=(0, 0))
    print(cesta)

    delay = 0.1
    if len(argv) > 1:
        try:
            delay = float(argv[1])
        except ValueError:
            pass
    for x in range(0, len(cesta)):
        pprint(str(x)+'. '+Hersik.post('/action', bot_id=Hersik.bot_id, action=cesta[x]).get('state'))
        sleep(delay)
