from common.item import Item, Character
from common.coordinates import Coord


class Ship(Item):
    pass


class Pirate(Character):
    def __init__(self, coordinates: Coord = None, gamer=None):
        Character.__init__(self, coordinates, gamer)
        self.step = 0
        self.locked = False


class Coin(Item):
    pass


class Chest(Item):
    pass
