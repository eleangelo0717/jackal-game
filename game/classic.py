from game.field import Generator, Coordinates, Field, Template
from pack.main import Pack, listGenerator

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
        tiles = self.fillTiles()
        self.field = Field(
            template=Template(generator=ClassicGenerator()),
            tilePack=Pack(listGenerator(tiles)))

    def fillTiles(self):
        items = []
        items += [tiles.tiles.Tile() for _ in range(18)]

        items += [tiles.tiles.TileRow([[1, 0]]) for _ in range(3)]
        items += [tiles.tiles.TileRow([[1, 1]]) for _ in range(3)]
        items += [tiles.tiles.TileRow(
            [[1, 0], [-1, 0]]
        ) for _ in range(3)]
        items += [tiles.tiles.TileRow(
            [[1, 1], [-1, -1]]
        ) for _ in range(3)]
        items += [tiles.tiles.TileRow(
            [[1, 1], [-1, 0], [0, -1]]
        ) for _ in range(3)]
        items += [tiles.tiles.TileRow(
            [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ) for _ in range(3)]
        items += [tiles.tiles.TileRow(
            [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        ) for _ in range(3)]

        items += [tiles.tiles.TileHorse() for _ in range(2)]

        items += [tiles.tiles.TileWhirl(2) for _ in range(5)]
        items += [tiles.tiles.TileWhirl(3) for _ in range(4)]
        items += [tiles.tiles.TileWhirl(4) for _ in range(2)]
        items += [tiles.tiles.TileWhirl(5) for _ in range(1)]

        items += [tiles.tiles.TileIce() for _ in range(6)]
        items += [tiles.tiles.TileTrap() for _ in range(3)]
        items += [tiles.tiles.TileCroco() for _ in range(4)]
        items += [tiles.tiles.TileCannibal() for _ in range(1)]
        items += [tiles.tiles.TileFort() for _ in range(2)]
        items += [tiles.tiles.TileFortAborigine() for _ in range(1)]

        items += [tiles.tiles.TileChest(1) for _ in range(5)]
        items += [tiles.tiles.TileChest(2) for _ in range(5)]
        items += [tiles.tiles.TileChest(3) for _ in range(3)]
        items += [tiles.tiles.TileChest(4) for _ in range(2)]
        items += [tiles.tiles.TileChest(5) for _ in range(1)]
        items += [tiles.tiles.TileTreasure()]

        items += [tiles.tiles.TileAirplane() for _ in range(1)]
        items += [tiles.tiles.TileBalloon() for _ in range(2)]
        items += [tiles.tiles.TileCannon() for _ in range(2)]
        items += [tiles.tiles.TileCarramba() for _ in range(1)]
        items += [tiles.tiles.TileLighthouse() for _ in range(1)]
        items += [tiles.tiles.TileCave() for _ in range(4)]
        items += [tiles.tiles.TileQuake() for _ in range(1)]
        items += [tiles.tiles.TileJungle() for _ in range(3)]
        items += [tiles.tiles.TileGrass() for _ in range(2)]

        items += [tiles.tiles.TileRum(1) for _ in range(3)]
        items += [tiles.tiles.TileRum(2) for _ in range(2)]
        items += [tiles.tiles.TileRum(3) for _ in range(1)]

        items += [tiles.tiles.TileBarrel() for _ in range(4)]

        items += [tiles.tiles.TileBenGunn()]
        items += [tiles.tiles.TileMissionary()]
        items += [tiles.tiles.TileFriday()]

        return items

    def fieldsInfo(self):
        return self.field.batchFieldInfo(
            Coordinates(0, 0),
            Coordinates(FIELD_DIMENSION-1, FIELD_DIMENSION-1))
