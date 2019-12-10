from items import Item
import moves

class Character(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, gamer, x, y)
        self.isCharacter = True

    def avaiableMoves(self, game):
        return []

class Pirate(Character):
    def __init__(self, gamer=None, x=None, y=None):
        Character.__init__(self, gamer, x, y)
        self.burder = None

    def avaiableMoves(self, game):
        result=[]
        if not self.isPlaced:
            return result
        fieldPlace = self.getPlace(game)
        if fieldPlace is None:
            return []

        if not game.field.isPlaceInField(self.x, self.y):
            return result
        if game.field.isPlaceGround(self.x, self.y):
            for move in moves.movesArrayWithDiagonales:
                x = self.x + move[0]
                y = self.y + move[1]
                if game.field.isPlaceGround(x, y) or (
                    game.field.isPlaceOcean(x, y) and game.haveOwnShip(x, y)
                    ):
                    result.append((x, y))
            return result
        if game.field.isPlaceOcean(self.x, self.y):
            if game.haveOwnShip(self.x, self.y):
                for move in moves.movesArray():
                    x = self.x + move[0]
                    y = self.y + move[1]
                    if game.field.isPlaceGround(x, y):
                        result.append((x, y))
            else:
                for move in moves.movesArrayWithDiagonales():
                    x = self.x + move[0]
                    y = self.y + move[1]
                    if game.field.isPlaceOcean(x, y):
                        result.append((x, y))                
            return result
        return result

class Missionary(Pirate):
    pass 


class Friday(Pirate):
    pass 
         

class BenGunn(Pirate):
    pass 
         

class Ship(Character):
    def __init__(self, gamer=None, x=None, y=None):
        Character.__init__(self, gamer, x, y)
        self.items = []
    
    def avaiableMoves(self, game):
        moves=[]
        if not self.isPlaced:
            return moves
        if not game.field.isPlaceInField(self.x, self.y):
            return moves
        for move in moves.movesArray():
            x = self.x + move[0]
            y = self.y + move[1]
            if game.field.isPlaceOcean(x, y) and game.field.isPlaceNearChest(x, y):
                moves.append((x, y))
        return moves
                    

        



