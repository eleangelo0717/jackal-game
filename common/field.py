class Place(object):
    def __init__(self, placeType=None, tile=None, opened=False):
        self.type = placeType
        self.tile = tile
        self.opened = opened

    def __repr__(self):
        return f"<{self.type}: {self.opened} {self.tile}>"

    def setTile(self, tile):
        self.tile = tile


class Field(object):
    def __init__(self, places=None):
        self.places = places

    