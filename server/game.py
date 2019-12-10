from field import Field
from gamer import Gamer
import characters
import moves

PLACES = [
    (6, 0),
    (12, 6),
    (6, 12),
    (0, 6)
]

class Game(object):
    def __init__(self):
        self.field = Field(game=self)
        self.items = []
        self.gamers = [Gamer(game=self, id=i, team=i) for i in range(4)]
        self.initItems()

    def initItems(self):
        for gamer in self.gamers:
            (x, y) = PLACES[gamer.id]
            self.items.append(characters.Ship(gamer=gamer, x=x, y=y))
            for _ in range(3):
                self.items.append(characters.Pirate(gamer=gamer, x=x, y=y))
