from game.classic import ClassicGame
from game.field import Coordinates
import datetime


class GameServer(object):
    def __init__(self):
        self.game = ClassicGame()
        self.ts = datetime.datetime.now()
        self.game.field.placeNextTile(Coordinates(1, 2)).opened = True
        self.game.field.placeNextTile(Coordinates(1, 3))

    def toDict(self):
        fieldInfo = self.game.fieldsInfo()
        return {
            'ts': self.ts,
            'field': [
                {'c': key,
                 'p': item.type,
                 't': {
                     'type': item.tile.className()
                 } if item.opened else None}
                for key, item in fieldInfo.items()
            ],
        }
