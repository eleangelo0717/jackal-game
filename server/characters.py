from items import Item

class Character(Item):
    def __init__(self, x=None, y=None):
        Item.__init__(self, x, y)


class Pirate(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
        self.burder = None


class Ship(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
