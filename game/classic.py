from game.field import Generator, Coordinates

from utils import distance
import tiles.tiles

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
        self.tiles += [tiles.tiles.Tile() for _ in range(18)]

        self.tiles += [tiles.tiles.TileRow([[1, 0]]) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow([[1, 1]]) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow(
            [[1, 0], [-1, 0]]
            ) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow(
            [[1, 1], [-1, -1]]
            ) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow(
            [[1, 1], [-1, 0], [0, -1]]
            ) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow(
            [[1, 0], [-1, 0], [0, 1], [0, -1]]
            ) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRow(
            [[1, 1], [-1, 1], [1, -1], [-1, -1]]
            ) for _ in range(3)]

        self.tiles += [tiles.tiles.TileHorse() for _ in range(2)]

        self.tiles += [tiles.tiles.TileWhirl(2) for _ in range(5)]
        self.tiles += [tiles.tiles.TileWhirl(3) for _ in range(4)]
        self.tiles += [tiles.tiles.TileWhirl(4) for _ in range(2)]
        self.tiles += [tiles.tiles.TileWhirl(5) for _ in range(1)]

        self.tiles += [tiles.tiles.TileIce() for _ in range(6)]
        self.tiles += [tiles.tiles.TileTrap() for _ in range(3)]
        self.tiles += [tiles.tiles.TileCroco() for _ in range(4)]
        self.tiles += [tiles.tiles.TileCannibal() for _ in range(1)]
        self.tiles += [tiles.tiles.TileFort() for _ in range(2)]
        self.tiles += [tiles.tiles.TileFortAborigine() for _ in range(1)]

        self.tiles += [tiles.tiles.TileChest(1) for _ in range(5)]
        self.tiles += [tiles.tiles.TileChest(2) for _ in range(5)]
        self.tiles += [tiles.tiles.TileChest(3) for _ in range(3)]
        self.tiles += [tiles.tiles.TileChest(4) for _ in range(2)]
        self.tiles += [tiles.tiles.TileChest(5) for _ in range(1)]
        self.tiles += [tiles.tiles.TileTreasure()]

        self.tiles += [tiles.tiles.TileAirplane() for _ in range(1)]
        self.tiles += [tiles.tiles.TileBalloon() for _ in range(2)]
        self.tiles += [tiles.tiles.TileCannon() for _ in range(2)]
        self.tiles += [tiles.tiles.TileCarramba() for _ in range(1)]
        self.tiles += [tiles.tiles.TileLighthouse() for _ in range(1)]
        self.tiles += [tiles.tiles.TileCave() for _ in range(4)]
        self.tiles += [tiles.tiles.TileQuake() for _ in range(1)]
        self.tiles += [tiles.tiles.TileJungle() for _ in range(3)]
        self.tiles += [tiles.tiles.TileGrass() for _ in range(2)]

        self.tiles += [tiles.tiles.TileRum(1) for _ in range(3)]
        self.tiles += [tiles.tiles.TileRum(2) for _ in range(2)]
        self.tiles += [tiles.tiles.TileRum(3) for _ in range(1)]

        self.tiles += [tiles.tiles.TileBarrel() for _ in range(4)]

        self.tiles += [tiles.tiles.TileBenGunn()]
        self.tiles += [tiles.tiles.TileMissionary()]
        self.tiles += [tiles.tiles.TileFriday()]

        return self.tiles
