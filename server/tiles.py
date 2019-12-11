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
    def __init__(self, place=None, angle=0):
        self.angle = angle
        self.place = None

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def className(self):
        return self.__class__.__name__

    def activate(self, character):
        pass



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

    def activate(self, character):
        for _ in range(self.money):
            coin = character.gamer.game.getFreeItem('Coin')
            if not coin:
                return None
            (coin.x, coin.y) = (self.place.x, self.place.y)
        return 0


class TileCardRum(TileCard):
    def __init__(self, bottles):
        TileCard.__init__(self)
        self.bottles = bottles

    def __repr__(self):
        return f"<{self.__class__.__name__} bottles:{self.bottles}>"

    def activate(self, character):
        for _ in range(self.bottles):
            bottle = character.gamer.game.getFreeItem('Bottle')
            if not bottle:
                return None
            (bottle.x, bottle.y) = (self.place.x, self.place.y)
            bottle.setCharacter(character.gamer.getShip())
        return 0


class TileCardTreasure(TileCard):
    def __init__(self):
        TileCard.__init__(self)

    def activate(self, character):
        treasure = character.gamer.game.getFreeItem('Treasure')
        if not treasure:
            return None
        (treasure.x, treasure.y) = (self.place.x, self.place.y)
        return 0


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

    def activate(self, character):
        return 1


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

    def activate(self, character):
        return 1


class TileCardIce(TileCard):
    def __init__(self):
        TileCard.__init__(self)

    def activate(self, character):
        return 1


class TileCardTrap(TileCard):
    def __init__(self):
        TileCard.__init__(self)


class TileCardCroco(TileCard):
    def __init__(self):
        TileCard.__init__(self)        

    def activate(self, character):
        (character.x, character.y) = (character._x, character._y)
        return 0


class TileCardCannibal(TileCard):
    def __init__(self):
        TileCard.__init__(self)    

    def activate(self, character):
        (character.x, character.y) = (None, None)
        return 0 


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

    def activate(self, character):
        p = character.gamer.game.getFreeItem('BenGunn')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0


class TileCardMissionary(TileCard):
    def __init__(self):
        TileCard.__init__(self)        

    def activate(self, character):
        p = character.gamer.game.getFreeItem('Missionary')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0

class TileCardFriday(TileCard):
    def __init__(self):
        TileCard.__init__(self)     

    def activate(self, character):
        p = character.gamer.game.getFreeItem('Friday')
        if not p:
            return None
        (p.x, p.y) = (self.place.x, self.place.y)
        p.gamer = character.gamer
        print(p)
        return 0

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



