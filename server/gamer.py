class Ship(object):
    def __init__(self):
        pass

class Pirate(object):
    def __init__(self):
        pass

class Gamer(object):
    def __init__(self, team=None):
        self.team = team
        self.ship = Ship()
        self.pirates = [Pirate() for i in range(3)]