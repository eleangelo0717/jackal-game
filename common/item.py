from common.coordinates import Coord, Move

class Item(object):
    def __init__(self, coordinates: Coord = None, gamer = None):
        self.coordinates = coordinates
        self.gamer = gamer

    def go(self, coordinates: Coord):
        self.coordinates = coordinates

    def to_json(self):
        result = {
            'type': f'{self.__class__.__name__}'
        }
        if (self.gamer is not None): result['gamer'] = self.gamer
        if (self.coordinates):
            result['x'] = self.coordinates.x
            result['y'] = self.coordinates.y
        return result


class ItemMove(object):
    def __init__(self, character: Item, move: Move, payload=None):
        self.character = character
        self.move = move
        self.payload = payload

    def __repr__(self):
        if (self.payload):
            return f"<{self.__class__.__name__} {self.character}+{self.payload} {self.move}>"

        return f"<{self.__class__.__name__} {self.character} {self.move}>"
