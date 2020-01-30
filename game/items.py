from common.item import Item, Character
from common.coordinates import Coord


class Ship(Item):
    pass


class Pirate(Character):
    def __init__(self, coordinates: Coord = None, gamer=None):
        Character.__init__(self, coordinates, gamer)
        self.step = 0
        self.locked = False

    def to_json(self):
        result = {
            'type': self.getClassName()
        }
        if (self.gamer is not None):
            result['gamer'] = self.gamer
        if (self.coordinates):
            result['x'] = self.coordinates.x
            result['y'] = self.coordinates.y
        if (self.step is not None):
            result['step'] = self.step
        return result


class Coin(Item):
    def __init__(self, coordinates: Coord = None, gamer=None):
        Item.__init__(self, coordinates, gamer)
        self.step = 0

    def to_json(self):
        result = {
            'type': self.getClassName()
        }
        if (self.gamer is not None):
            result['gamer'] = self.gamer
        if (self.coordinates):
            result['x'] = self.coordinates.x
            result['y'] = self.coordinates.y
        if (self.step is not None):
            result['step'] = self.step
        return result


class Chest(Item):
    def __init__(self, coordinates: Coord = None, gamer=None):
        Item.__init__(self, coordinates, gamer)
        self.step = 0
