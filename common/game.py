from common.field import Field
from common.item import ItemMove
import json

class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        if "to_json" in dir(obj):
            return obj.to_json()

        return json.JSONEncoder.default(self, obj)


class Game(object):
    def __init__(self, field: Field = {}, items = [], gamers = []):
        self.field = field
        self.items = items
        self.gamers = gamers

    def moveItem(self, itemMove: ItemMove):
        if not self.checkMove(itemMove):
           return False
        itemMove.item.go(itemMove.move.destination)

    def checkMove(self, itemMove: ItemMove):
        return True

    def to_json(self):
        return {
            'field': json.dumps(self.field),
            'items': json.dumps(self.items),
            'gamers': json.dumps(self.gamers)
        }

    def dumps(self):
        return json.dumps(self, cls=GameEncoder)
