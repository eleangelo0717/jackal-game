from items import Item, checkPlaced
import moves

class Character(Item):
    def __init__(self, gamer=None, x=None, y=None):
        Item.__init__(self, gamer, x, y)
        self.isCharacter = True

    def avaiableMoves(self):
        return []

    def getItems(self):
        return [item for item in self.gamer.game.items if item.character == self]

class Pirate(Character):
    def __init__(self, gamer=None, x=None, y=None):
        Character.__init__(self, gamer, x, y)
        self.burder = None
    
    @checkPlaced
    def avaiableMoves(self):
        result=[]
        fieldPlace = self.getPlace()
        if not fieldPlace:
            return []
        if fieldPlace.isGround():
            result += [
                moves.Move(p.x, p.y) 
                for p 
                in fieldPlace.getNeighboringPlaces(moves.directions8)
                if p and (p.isGround() or (p.isSea() and p.hasTeamShip(self.gamer.team)))
                ]
        else:
            if fieldPlace.hasTeamShip(self.gamer.team):
                result += [moves.Move(p.x, p.y) for p in
                        [place 
                        for place 
                        in fieldPlace.getNeighboringPlaces(moves.directions4)
                        if place
                        ]
                    if p and p.isGround()
                    ]
            else:
                result +=  [moves.Move(p.x, p.y) for p in
                        [place 
                        for place 
                        in fieldPlace.getNeighboringPlaces(moves.directions8)
                        if place
                        ]
                    if p and p.isSea()
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
    
    @checkPlaced
    def avaiableMoves(self):
        result=[]
        fieldPlace = self.getPlace()
        if not fieldPlace:
            return []
        result += [moves.Move(p.x, p.y) for p in
                [place 
                for place 
                in fieldPlace.getNeighboringPlaces(moves.directions4)
                if place
                ]
            if p and not p.isGround() and 
                len([pn for pn in p.getNeighboringPlaces(moves.directions4) if pn and pn.isGround()]) > 0]
        return list(set(result))
                    

        



