from field import Field
from gamer import Gamer


class Game(object):
    def __init__(self):
        self.field = Field()
        self.gamers = [Gamer(id=i, team=i) for i in range(4)]
        self.field = Field()

    def avaiableMoves(self, gamer):
        moves = []
        moves = moves + [{'character': gamer.ship, 'move': move} for move in gamer.ship.avaiableMoves(self)]
        for pirate in gamer.pirates:
            moves = moves + [{'character': pirate, 'move': move} for move in pirate.avaiableMoves(self)]
        return moves

    def haveOwnShip(self, x, y):
        return False