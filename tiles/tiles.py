from common.tile import Tile
from common.coordinates import DeltaCoord

from functools import partial


class TileEmpty(Tile):
    def __init__(self, kind=0):
        Tile.__init__(self)
        self.kind = kind

    def to_json(self):
        result = {
            'type': f"{self.getClassName()}{self.kind}"
        }
        return result


class TileCoins(Tile):
    def __init__(self, money):
        Tile.__init__(self)
        self.money = money

    def onOpen(self, game):
        return partial(game.placeCoins, money=self.money)

    def to_json(self):
        result = {
            'type': f"{self.getClassName()}{self.money}"
        }
        return result


class TileWhirl(Tile):
    def __init__(self, kind=0):
        Tile.__init__(self)
        self.kind = kind

    def to_json(self):
        result = {
            'type': f"{self.getClassName()}{self.kind}"
        }
        return result


class TileRum(Tile):
    def __init__(self, bottles):
        Tile.__init__(self)
        self.bottles = bottles

    def to_json(self):
        result = {
            'type': f"{self.getClassName()}{self.bottles}"
        }
        return result


class TileTreasure(Tile):
    def __init__(self):
        Tile.__init__(self)

    def onOpen(self, game):
        return partial(game.placeChest)


class TileArrow(Tile):
    def __init__(self, directions: [DeltaCoord], angle=0):
        Tile.__init__(self, angle)
        self.directions = directions

    def to_json(self):

        result = {
            'type': f"{self.getClassName()}{len(self.directions)}{self.directions[0].y}"
        }
        return result


class TileAirplane(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCannon(Tile):
    def __init__(self, angle=0):
        Tile.__init__(self, angle)


class TileHorse(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileIce(Tile):
    def __init__(self):
        Tile.__init__(self)


class TilePitfall(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCroco(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCannibal(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileFort(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileFortAborigine(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCarramba(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileBalloon(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileLighthouse(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileBenGunn(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileMissionary(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileFriday(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileBarrel(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCave(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileQuake(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileJungle(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileGrass(Tile):
    def __init__(self):
        Tile.__init__(self)
