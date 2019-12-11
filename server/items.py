import moves

def checkPlaced(f):
    def wrapper(*args):
        item = args[0]
        if not item.isPlaced():
            return []
        return f(*args)
    return wrapper

class Item(object):
    def __init__(self, gamer=None, x=None, y=None):
        self.gamer = gamer
        self.x = x
        self.y = y
        self._x = None
        self._y = None
        self.character = None
        self.isCharacter = False
        self.moveable = False

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.gamer and self.gamer.id} [{self.x}:{self.y}]>"

    def className(self):
        return self.__class__.__name__

    def move(self, x, y):
        (self.x, self.y) = (x, y)

    def getPlace(self):
        return self.gamer.game.field.getPlaceByCoordinates(self.x, self.y)

    def isPlaced(self):
        return not (self.x is None or self.y is None)

    def setCharacter(self, character):
        self.character = character
        if character:
            self.gamer = character.gamer
            self.x = character.x
            self.y = character.y
        else:
            self.gamer = None
        return self


class Coin(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, x, y)
        self.moveable = True
        self.price = 1


class Treasure(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, x, y)
        self.moveable = True
        self.price = 3

class Bottle(Item):
    pass

