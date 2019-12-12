from game.field import Generator, Coordinates

from utils import distance
import tiles.tile


FIELD_DIMENSION = 13


class ClassicGenerator(Generator):

    def next(self, coordinates: Coordinates = None):
        m = FIELD_DIMENSION // 2
        (dx, dy) = (distance(m, coordinates.x), distance(m, coordinates.y))
        if dx > m or dy > m or (dx == m and dy == m):
            return 'EXCLUDED'
        if dx == m or dy == m or (dx == m-1 and dy == m-1):
            return 'SEA'
        return 'GROUND'


class ClassicGame(object):
    def __init__(self):
        self.tiles = []

    def fillTiles(self):
        self.tiles += [tiles.tile.Tile() for _ in range(20)]
        return self.tiles
