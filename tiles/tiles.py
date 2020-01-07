from common.tile import Tile
from common.direction import Direction4

import random


class TileWhirl(Tile):
    def __init__(self, moves):
        Tile.__init__(self)
        self.moves = moves

    def __repr__(self):
        return f"<{self.__class__.__name__} moves:{self.moves}>"


class TileChest(Tile):
    def __init__(self, money):
        Tile.__init__(self)
        self.money = money

    def __repr__(self):
        return f"<{self.__class__.__name__} money:{self.money}>"


class TileRum(Tile):
    def __init__(self, bottles):
        Tile.__init__(self)
        self.bottles = bottles

    def __repr__(self):
        return f"<{self.__class__.__name__} bottles:{self.bottles}>"


class TileTreasure(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileRow(Tile):
    def __init__(self, directionsFormulae, angle=None):
        if angle is None:
            angle = random.randint(0, 3)
        Tile.__init__(self, angle)
        self.directions = []
        for formula in directionsFormulae:
            direction = Direction4(formula[0], formula[1], angle)
            self.directions.append(direction)

    def __repr__(self):
        return f"<{self.__class__.__name__} directions:{len(self.directions)}>"

    def activate(self, character):
        self.action(character)
        return 1

    def action(self, character):
        return 0


class TileAirplane(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCannon(Tile):
    def __init__(self, angle=None):
        if angle is None:
            angle = random.randint(0, 3)
        Tile.__init__(self, angle)
        self.direction = Direction4(1, 0, angle)


class TileHorse(Tile):
    def __init__(self):
        Tile.__init__(self)

    def activate(self, character):
        return 1


class TileIce(Tile):
    def __init__(self):
        Tile.__init__(self)

    def action(self, character):
        move = Move(character.x * 2 - character._x, character.y * 2 -
                    character._y, character.lastMove.payload)
        character.move(move, force=True)
        return


class TileTrap(Tile):
    def __init__(self):
        Tile.__init__(self)


class TileCroco(Tile):
    def __init__(self):
        Tile.__init__(self)

    def action(self, character):
        (character.x, character.y) = (character._x, character._y)
        return


class TileCannibal(Tile):
    def __init__(self):
        Tile.__init__(self)

    def action(self, character):
        (character.x, character.y) = (None, None)
        return 0


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

    def activate(self, character):
        p = character.gamer.game.getFreeItem('BenGunn')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0


class TileMissionary(Tile):
    def __init__(self):
        Tile.__init__(self)

    def activate(self, character):
        p = character.gamer.game.getFreeItem('Missionary')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0


class TileFriday(Tile):
    def __init__(self):
        Tile.__init__(self)

    def activate(self, character):
        p = character.gamer.game.getFreeItem('Friday')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0


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
