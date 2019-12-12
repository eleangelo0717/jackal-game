from game.field import Generator, Coordinates

from utils import distance


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

