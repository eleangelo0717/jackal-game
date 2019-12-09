class Item(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.__class__.__name__} [{self.x},{self.y}]>"

    def Move(self, x, y):
        (self.x, self.y) = (x, y)


class Coin(Item):
    def __init__(self, x=None, y=None):
        Item.__init__(self, x, y)
        self.price = 1


class Chest(Item):
    def __init__(self,x=None, y=None):
        Item.__init__(self, x, y)
        self.price = 3

