from common.coordinates import Coord

class Place(object):
    def __init__(self, placeType=None, tile=None, opened=False):
        self.type = placeType
        self.tile = tile
        self.opened = opened

    def __repr__(self):
        return f"<{self.type}: {self.opened} {self.tile}>"

    def setTile(self, tile):
        self.tile = tile

    def to_json(self):
        return {
            'type': self.type,
            'tile': self.tile,
            'opened': self.opened
        }


class Field(object):
    def __init__(self, places={}):
        self.places = places

    def to_json(self):
        return [
            [self.places.get(Coord(x,y))
                for y in set(key.y for key in self.places.keys())
                ]
            for x in set(key.x for key in self.places.keys())
            ]

