from game.main import Game
from common.coordinates import Coord
from common.utils import GameEncoder
import datetime
import json
import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler

GS = {}


class GameServer(object):
    def __init__(self):
        self.game = Game()
        self.ts = datetime.datetime.now()

    def move(self, item: int, x: int, y: int):
        return self.game.moveItem(item, Coord(x, y))

    def to_json(self):
        info = self.game.to_json()
        info['ts'] = f'{self.ts}'
        return info


class Handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin',
                         '*')
        self.send_header("Access-Control-Allow-Headers",
                         "Origin, X-Requested-With, Content-Type, Accept")
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(game.to_json(), cls=GameEncoder).encode())

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = json.loads(self.data_string)
        if isinstance(data, list):
            for m in data:
                item = int(m.get('item'))
                x = int(m.get('x'))
                y = int(m.get('y'))
                success = game.move(item, x, y)
        else:        
            item = int(data.get('item'))
            x = int(data.get('x'))
            y = int(data.get('y'))
            success = game.move(item, x, y)
        result = game.to_json()
        result['success'] = success

        self.wfile.write(json.dumps(result, cls=GameEncoder).encode())


def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


game = GS.get(id, GameServer())

if __name__ == "__main__":
    run()
