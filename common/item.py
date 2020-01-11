from common.coordinates import Coord, Move

class Item(object):
    def __init__(self, coordinates: Coord = None):
        self.coordinates = coordinates

    def go(self, coordinates: Coord):
        self.coordinates = coordinates


class ItemMove(object):
    def __init__(self, character: Item, move: Move, payload=None):
        self.character = character
        self.move = move
        self.payload = payload

    def __repr__(self):
        if (self.payload):
            return f"<{self.__class__.__name__} {self.character}+{self.payload} {self.move}>"

        return f"<{self.__class__.__name__} {self.character} {self.move}>"
