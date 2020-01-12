from common.field import Field
from common.item import ItemMove
from common.utils import GameEncoder
from common.coordinates import Coord, Move
import json


class Game(object):
    def __init__(self, field: Field = {}, items = {}, gamers = []):
        self.field = field
        self.items = items
        self.gamers = gamers
        self.turn = 0
        self.status = None
        self.log = []

    def moveItem(self, itemId: int, destination: Coord):
        item = self.items.get(itemId)
        if not (item): return False
        itemMove = ItemMove(item, Move(start=item.coordinates, destination=destination))
        if not self.checkMove(itemMove):
           return False
        itemMove.accept()
        self.logMove(itemMove)

    def checkMove(self, itemMove: ItemMove):
        return True

    def changeTurn(self):
        self.turn = (self.turn + 1) % len(self.gamers)
        return self

    def to_json(self):
        return {
            'field': self.field,
            'items': self.items,
            'gamers': self.gamers,
            'status': self.status,
            'turn': self.turn
        }

    def dumps(self):
        return json.dumps(self, cls=GameEncoder)

    def logMove(self, itemMove: ItemMove):
        logRecord = {
            'turn': self.turn,
            'item': {
                'class': itemMove.item.getClassName()
            },
            'coordinates': {
                'x': itemMove.move.destination.x,
                'y': itemMove.move.destination.y
            }
        }
        self.log += [logRecord]
        print(logRecord)
        return logRecord