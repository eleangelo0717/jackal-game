from items import Item, checkPlaced
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
    
    @checkPlaced
    def avaiableMoves(self, game):
        result=[]
        fieldPlace = self.getPlace(game)
        if fieldPlace is None:
            return []
        if fieldPlace.isGround:
            result = result + [
                moves.Move(p.x, p.y) 
                for p 
                in game.field.getNeighboringPlaces(fieldPlace, moves.movesArrayWithDiagonales)
                if p.isGround or (not p.isGround and game.hasOwnShip(p, self))
                ]
        else:
            if game.hasOwnShip(fieldPlace, self):
                result = result + [
                    moves.Move(p.x, p.y) 
                    for p 
                    in game.field.getNeighboringPlaces(fieldPlace, moves.movesArray)
                    if p.isGround
                    ]
            else:
                result = result + [
                    moves.Move(p.x, p.y) 
                    for p 
                    in game.field.getNeighboringPlaces(fieldPlace, moves.movesArrayWithDiagonales)
                    if not p.isGround
                    ]              
        return list(set(result))

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
    
    @checkPlaced
    def avaiableMoves(self, game):
        result=[]
        fieldPlace = self.getPlace(game)
        if fieldPlace is None:
            return []
        result = result + [
                moves.Move(p.x, p.y) 
                for p 
                in game.field.getNeighboringPlaces(fieldPlace, moves.movesArray)
                if not p.isGround and game.field.isPlaceNearChest(p.x, p.y)
                ]
        return list(set(result))
                    

        



