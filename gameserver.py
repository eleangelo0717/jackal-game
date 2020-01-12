from game.main import Game
from common.coordinates import Coord
import datetime

class GameServer(object):
    def __init__(self):
        self.game = Game()
        self.ts = datetime.datetime.now()

    def to_json(self):
        info = self.game.to_json()
        info['ts'] = f'{self.ts}'
        return info