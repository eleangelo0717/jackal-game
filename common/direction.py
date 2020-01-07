class Direction4(object):
    def __init__(self, x, y, rotate=0):
        angleFunc = [
            (x, y),
            (y, -x),
            (-x, -y),
            (-y, x)
        ]
        (self.x, self.y) = angleFunc[rotate]


class Move(object):
    def __init__(self, x, y, payload = None):
        self.x = x
        self.y = y
        self.payload = payload

    def __repr__(self):
        return f"<{self.__class__.__name__} [{self.x}:{self.y}] {self.payload}>"


class CharacterMove(object):
    def __init__(self, character, move):
        self.character = character
        self.move = move

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.character} [{self.move.x}:{self.move.y}]>"

directions4 = [Move(1,0), Move(-1,0), Move(0,1), Move(0,-1)]
directions8 = [Move(1,0), Move(1, 1), Move(-1,0), Move(-1,1), Move(0,1), Move(-1,-1), Move(0,-1), Move(1,-1)]
