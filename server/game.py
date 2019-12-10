from field import Field
from gamer import Gamer
import characters
import moves

places = [
    (6, 0),
    (12, 6),
    (6, 12),
    (0, 6)
]

class Game(object):
    def __init__(self):
        self.field = Field()
        self.items = []
        self.gamers = [Gamer(id=i, team=i) for i in range(4)]
        self.initItems()

    def initItems(self):
        for gamer in self.gamers:
            (x, y) = places[gamer.id]
            self.items.append(characters.Ship(gamer=gamer, x=x, y=y))
            for i in range(3):
                self.items.append(characters.Pirate(gamer=gamer, x=x, y=y))


    def gamerCharacters(self, gamer):
        return [item for item in self.items if item.gamer == gamer and item.isCharacter]


    def avaiableMoves(self, gamer):
        gamerCharacters = self.gamerCharacters(gamer)
        result = []
        for character in gamerCharacters:
            result = result + [moves.CharacterMove(character=character, move=move) for move in character.avaiableMoves(game=self)]
        return result


    def hasOwnShip(self, fieldPlace, item):
        for i in self.items:
            if i.x == fieldPlace.x and i.y == fieldPlace.y and i.gamer == item.gamer:
                return True
        return False
