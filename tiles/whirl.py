from common.tile import Tile

class WhirlTile(Tile):
    def __init__(self, moves=1):
        Tile.__init__(self)
        self.moves = moves

    def __repr__(self):
        return f"<{self.__class__.__name__} moves:{self.moves}>"

