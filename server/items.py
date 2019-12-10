class Item(object):
    def __init__(self, gamer=None, x=None, y=None):
        self.x = x
        self.y = y
        self.gamer = gamer
        self.isCharacter = False

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.gamer and self.gamer.id } [{self.x},{self.y}]>"

    def Move(self, x, y):
        (self.x, self.y) = (x, y)

    def getPlace(self, game):
        return game.getPlace(self.x, self,y)
        
    def isPlaced(self):
        return not (self.x is None or self.y is None)


class Coin(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, x, y)
        self.price = 1


class Chest(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, x, y)
        self.price = 3



