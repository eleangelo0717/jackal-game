import characters

class Gamer(object):
    def __init__(self, id, team=None):
        places = [
            (6, 0),
            (12, 6),
            (6, 12),
            (0, 6)
        ]
        self.id = id
        self.team = team
        (x, y) = places[self.id]
        self.ship = characters.Ship(x=x, y=y)
        self.pirates = [characters.Pirate(x=x, y=y) for i in range(3)]
        self.items = []

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.team} Pirates:{len(self.pirates)}>"


