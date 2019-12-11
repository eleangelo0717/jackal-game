import moves

class Gamer(object):
    def __init__(self, game, id, team=None):
        self.game = game
        self.id = id
        self.team = team
        self.angle = id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"

    def getItems(self):
        return [item for item in self.game.items if item.gamer == self]

    def getCharacters(self):
        return [item for item in self.getItems() if item.isCharacter]

    def getShip(self):
        return [item for item in self.getItems() if item.className() == 'Ship'][0]

    def availableMoves(self):
        result = []
        for character in self.getCharacters():
            result += [moves.CharacterMove(character=character, move=move) for move in character.availableMoves()]
        return result

