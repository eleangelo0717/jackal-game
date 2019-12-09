from items import Item

import utils

class Character(Item):
    def __init__(self, x=None, y=None):
        Item.__init__(self, x, y)


class Pirate(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
        self.burder = None

    def avaiableMoves(self, game):
        moves=[]
        if not self.isPlaced:
            return moves
        if not game.field.isPlaceInField(self.x, self.y):
            return moves
        if game.field.isPlaceGround(self.x, self.y):
            for move in utils.getMovesArrayWithDiagonales():
                x = self.x + move[0]
                y = self.y + move[1]
                if game.field.isPlaceGround(x, y) or (
                    game.field.isPlaceOcean(x, y) and game.haveOwnShip(x, y)
                    ):
                    moves.append((x, y))
            return moves
        if game.field.isPlaceOcean(self.x, self.y):
            if game.haveOwnShip(self.x, self.y):
                for move in utils.getMovesArray():
                    x = self.x + move[0]
                    y = self.y + move[1]
                    if game.field.isPlaceGround(x, y):
                        moves.append((x, y))
            else:
                for move in utils.getMovesArrayWithDiagonales():
                    x = self.x + move[0]
                    y = self.y + move[1]
                    if game.field.isPlaceOcean(x, y):
                        moves.append((x, y))                
            return moves
        

        return moves

class Missionary(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   


class Friday(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   
         

class BenGunn(Pirate):
    def __init__(self, x=None, y=None):
        Pirate.__init__(self, x, y)   
         

class Ship(Character):
    def __init__(self, x=None, y=None):
        Character.__init__(self, x, y)
    
    def avaiableMoves(self, game):
        moves=[]
        if not self.isPlaced:
            return moves
        if not game.field.isPlaceInField(self.x, self.y):
            return moves
        for move in utils.getMovesArray():
            x = self.x + move[0]
            y = self.y + move[1]
            if game.field.isPlaceOcean(x, y) and game.field.isPlaceNearChest(x, y):
                moves.append((x, y))
        return moves
                    

        



