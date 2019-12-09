from items import Item

class Character(Item):
    def __init__(self, x=None, y=None):
        Item.__init__(self, x, y)


class Pirate(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
        self.burder = None


class Missionary(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   


class Friday(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   
         

class BenGunn(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   
         

class Ship(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
