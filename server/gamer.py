import characters


class Gamer(object):
    def __init__(self, team=None):
        self.team = team
        self.ship = characters.Ship()
        self.pirates = [characters.Pirate() for i in range(3)]

    def __repr__(self):
        return f"<{self.__class__.__name__} Pirates:{len(self.pirates)}>"