class Character(object):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class Pirate(Character):
    def __init__(self):
        Character.__init__(self)


class Ship(Character):
    def __init__(self):
        Character.__init__(self)
