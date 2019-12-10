
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

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.character} [{self.move.x}:{self.move.y}]>"

directions4 = [Move(1,0), Move(-1,0), Move(0,1), Move(0,-1)]
directions8 = [Move(1,0), Move(1, 1), Move(-1,0), Move(-1,1), Move(0,1), Move(-1,-1), Move(0,-1), Move(1,-1)]