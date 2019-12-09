class Item(object):
    def __init__(self):
        self.tile = None

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class Coin(Item):
    def __init__(self):
        Item.__init__(self)
        self.price = 1


class Chest(Item):
    def __init__(self):
        Item.__init__(self)
        self.price = 3

