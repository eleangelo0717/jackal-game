class Gamer(object):
    def __init__(self, id, team=None):
        self.id = id
        self.team = team

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


