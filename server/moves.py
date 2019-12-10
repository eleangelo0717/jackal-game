movesArray = [(1,0), (-1,0), (0,1), (0,-1)]
movesArrayWithDiagonales = [(1,0), (1, 1), (-1,0), (-1,1), (0,1), (-1,-1), (0,-1), (1,-1)]

class Move(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<{self.__class__.__name__} [{self.x}:{self.y}]>"

class CharacterMove(object):
    def __init__(self, character, move):
        self.character = character
        self.move = move
