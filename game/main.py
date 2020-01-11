import common.game
from common.field import Field, Place
from common.coordinates import Coord
from common.utils import distance

FIELD_SIZE = 13

class Game(common.game.Game):
    def __init__(self):
        self.size = FIELD_SIZE
        field = self.generateField()
        items = []
        gamers = [i for i in range(0,4)]
        common.game.Game.__init__(self, field=field, items=items, gamers=gamers)
        
    def generateField(self):
        return Field(places={Coord(x,y): Place(self.getPlaceType(Coord(x,y))) 
            for x in range(0,self.size) 
            for y in range(0,self.size)
            })

    def getPlaceType(self, coord: Coord):
        m = self.size // 2
        (dx, dy) = (distance(m, coord.x), distance(m, coord.y))
        if dx > m or dy > m or (dx == m and dy == m):
            return 'EXCLUDED'
        if dx == m or dy == m or (dx == m-1 and dy == m-1):
            return 'SEA'
        return 'GROUND'
        