import random

from pack import Pack

class Direction(object):
    def __init__(self, x, y, angle=0):
        angleFunc = [
            (x, y),
            (y, -x),
            (-x, -y),
            (-y, x)
        ]
        (self.x, self.y) = angleFunc[angle]


class TileCard(object):
    def __init__(self, angle=0):
        self.angle = angle

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def className(self):
        return self.__class__.__name__


class TileCardWhirl(TileCard):
    def __init__(self, moves):
        TileCard.__init__(self)
        self.moves = moves

    def __repr__(self):
        return f"<{self.__class__.__name__} moves:{self.moves}>"


class TileCardChest(TileCard):
    def __init__(self, money):
        TileCard.__init__(self)
        self.money = money

    def __repr__(self):
        return f"<{self.__class__.__name__} money:{self.money}>"


class TileCardRum(TileCard):
    def __init__(self, bottles):
        TileCard.__init__(self)
        self.bottles = bottles

    def __repr__(self):
        return f"<{self.__class__.__name__} bottles:{self.bottles}>"


class TileCardTreasure(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardRow(TileCard):
    def __init__(self, directionsFormulae):
        angle = random.randint(0,3)
        TileCard.__init__(self, angle)
        self.directions = []
        for formula in directionsFormulae:
            direction = Direction(formula[0], formula[1], angle)
            self.directions.append(direction)

    def __repr__(self):
        return f"<{self.__class__.__name__} directions:{len(self.directions)}>"


class TileCardAirplane(TileCard):
    def __init__(self):
        TileCard.__init__(self)   


class TileCardCannon(TileCard):
    def __init__(self):
        angle = random.randint(0,3)
        TileCard.__init__(self, angle)   
        self.direction = Direction(1, 0, angle)


class TileCardHorse(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardIce(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardTrap(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardCroco(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardCannibal(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardFort(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardFortAborigine(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardCarramba(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardBalloon(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardLighthouse(TileCard):
    def __init__(self):
        TileCard.__init__(self)     


class TileCardBenGunn(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardMissionary(TileCard):
    def __init__(self):
        TileCard.__init__(self)        


class TileCardFriday(TileCard):
    def __init__(self):
        TileCard.__init__(self)     


class TileCardBarrel(TileCard):
    def __init__(self):
        TileCard.__init__(self)   


class TileCardCave(TileCard):
    def __init__(self):
        TileCard.__init__(self)   


class TileCardQuake(TileCard):
    def __init__(self):
        TileCard.__init__(self)   


class TileCardJungle(TileCard):
    def __init__(self):
        TileCard.__init__(self)  


class TileCardGrass(TileCard):
    def __init__(self):
        TileCard.__init__(self)  


class TilesPack(Pack):

    def __init__(self):
        Pack.__init__(self, [])
        self._generate()
        self.Shuffle()

    def _generate(self):
        self.items = self.items + [TileCard() for i in range(18)]

        self.items = self.items + [TileCardRow([[1, 0]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 1]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 0], [-1, 0]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 1], [-1, -1]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 1], [-1, 0], [0, -1]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 0], [-1, 0], [0, 1], [0, -1]]) for i in range(3)]
        self.items = self.items + [TileCardRow([[1, 1], [-1, 1], [1, -1], [-1, -1]]) for i in range(3)]

        self.items = self.items + [TileCardHorse() for i in range(2)]

        self.items = self.items + [TileCardWhirl(2) for i in range(5)]
        self.items = self.items + [TileCardWhirl(3) for i in range(4)]
        self.items = self.items + [TileCardWhirl(4) for i in range(2)]
        self.items = self.items + [TileCardWhirl(5) for i in range(1)]

        self.items = self.items + [TileCardIce() for i in range(6)]
        self.items = self.items + [TileCardTrap() for i in range(3)]
        self.items = self.items + [TileCardCroco() for i in range(4)]
        self.items = self.items + [TileCardCannibal() for i in range(1)]
        self.items = self.items + [TileCardFort() for i in range(2)]
        self.items = self.items + [TileCardFortAborigine() for i in range(1)]

        self.items = self.items + [TileCardChest(1) for i in range(5)]
        self.items = self.items + [TileCardChest(2) for i in range(5)]
        self.items = self.items + [TileCardChest(3) for i in range(3)]
        self.items = self.items + [TileCardChest(4) for i in range(2)]
        self.items = self.items + [TileCardChest(5) for i in range(1)]
        self.items = self.items + [TileCardTreasure()]

        self.items = self.items + [TileCardAirplane() for i in range(1)]
        self.items = self.items + [TileCardBalloon() for i in range(2)]
        self.items = self.items + [TileCardCannon() for i in range(2)]
        self.items = self.items + [TileCardCarramba() for i in range(1)]
        self.items = self.items + [TileCardLighthouse() for i in range(1)]
        self.items = self.items + [TileCardCave() for i in range(4)]
        self.items = self.items + [TileCardQuake() for i in range(1)]
        self.items = self.items + [TileCardJungle() for i in range(3)]
        self.items = self.items + [TileCardGrass() for i in range(2)]

        self.items = self.items + [TileCardRum(1) for i in range(3)]
        self.items = self.items + [TileCardRum(2) for i in range(2)]
        self.items = self.items + [TileCardRum(3) for i in range(1)]

        self.items = self.items + [TileCardBarrel() for i in range(4)]

        self.items = self.items + [TileCardBenGunn()]
        self.items = self.items + [TileCardMissionary()]
        self.items = self.items + [TileCardFriday()]



