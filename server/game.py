from field import Field
from gamer import Gamer


class Game(object):
    def __init__(self):
        self.field = Field()
        self.gamers = [Gamer() for i in range(4)]
        self.field = Field()
        