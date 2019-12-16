from dataclasses import dataclass
from random import randint
from utils import distance

FIELD_TYPES = {
    'EXCLUDED': {},
    'SEA': {},
    'GROUND': {}
}


@dataclass(eq=True, frozen=True)
class Coordinates:
    x: int
    y: int


class Generator(object):
    def next(self, coordinates: Coordinates = None):
        keys = fieldTypesKeys()
        return keys[0]


class RandomGenerator(Generator):
    def next(self, coordinates: Coordinates = None):
        keys = fieldTypesKeys()
        return keys[randint(0, len(FIELD_TYPES))]


class Place(object):
    def __init__(self, placeType=None, tile=None, opened=False):
        self.type = placeType
        self.tile = tile
        self.opened = opened

    def __repr__(self):
        return f"<{self.type}: {self.opened} {self.tile}>"

    def setTile(self, tile):
        self.tile = tile


class Template(object):
    def __init__(self, generator=Generator()):
        self._generator = generator
        self.places = {}

    def setPlace(self, coordinates: Coordinates, placeType):
        place = Place(placeType=placeType)
        self.places[coordinates] = place
        return place

    def getPlace(self, coordinates: Coordinates):
        place = self.places.get(coordinates)
        if not place:
            placeType = self._generator.next(coordinates)
            if placeType:
                place = self.setPlace(coordinates, placeType)
        return place

    def setPlaceTile(self, coordinates: Coordinates, tile):
        place = self.getPlace(coordinates)
        place.tile = tile


class Field(object):

    def __init__(self, template, tilePack):
        self.template = template
        self.tilePack = tilePack

    def fieldInfo(self, coordinates: Coordinates):
        place = self.template.getPlace(coordinates)
        return place

    def batchFieldInfo(self, c1: Coordinates, c2: Coordinates):
        x1, x2 = min([c1.x, c2.x]), max([c1.x, c2.x])
        y1, y2 = min([c1.y, c2.y]), max([c1.y, c2.y])
        result = {}
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                c = Coordinates(x, y)
                result[c] = self.fieldInfo(c)
        return result

    def placeNextTile(self, coordinates: Coordinates, force=False):
        place = self.template.getPlace(coordinates)
        if force or not place.tile:
            tile = self.tilePack.next()
            place.tile = tile
        return place


def fieldTypesKeys():
    return list(FIELD_TYPES.keys())
