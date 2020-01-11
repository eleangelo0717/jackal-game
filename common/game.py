from common.field import Field
from common.item import ItemMove
from common.utils import GameEncoder
import json


class Game(object):
    def __init__(self, field: Field = {}, items = [], gamers = []):
        self.field = field
        self.items = items
        self.gamers = gamers
        self.status = None

    def moveItem(self, itemMove: ItemMove):
        if not self.checkMove(itemMove):
           return False
        itemMove.item.go(itemMove.move.destination)

    def checkMove(self, itemMove: ItemMove):
        return True

    def to_json(self):
        return {
            'field': self.field,
            'items': json.dumps(self.items, cls=GameEncoder),
            'gamers': json.dumps(self.gamers, cls=GameEncoder),
            'status': json.dumps(self.status, cls=GameEncoder)
        }

    def dumps(self):
        return json.dumps(self, cls=GameEncoder)
