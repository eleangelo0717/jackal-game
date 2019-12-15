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


class Template(object):
    def __init__(self, generator=Generator()):
        self._generator = generator
        self.places = {}

    def setPlace(self, coordinates: Coordinates, fieldType):
        place = FIELD_TYPES[fieldType]
        self.places[coordinates] = place
        return self

    def getPlace(self, coordinates: Coordinates):
        place = self.places.get(coordinates)
        if not place:
            place = self._generator.next(coordinates)
            if place:
                self.setPlace(coordinates, place)
        return place


class Field(object):

    def __init__(self, template, tilePack):
        self.template = template
        self.tilePack = tilePack

    def fieldInfo(self, coordinates: Coordinates):
        place = self.template.getPlace(coordinates)
        tile = None
        return (place, tile)

    def batchFieldInfo(self, c1: Coordinates, c2: Coordinates):
        x1, x2 = min([c1.x, c2.x]), max([c1.x, c2.x])
        y1, y2 = min([c1.y, c2.y]), max([c1.y, c2.y])
        result = {}
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                c = Coordinates(x, y)
                fieldInfo = self.fieldInfo(c)
                result[c] = {
                    'place': fieldInfo[0],
                    'tile': fieldInfo[1]
                }
        return result


def fieldTypesKeys():
    return list(FIELD_TYPES.keys())
