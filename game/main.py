import common.game
from common.field import Field, Place
from common.coordinates import Coord
from common.utils import distance
from common.tile import Tile
from common.item import Item

FIELD_SIZE = 13

class Game(common.game.Game):
    def __init__(self):
        self.size = FIELD_SIZE
        field = self.generateField()
        gamers = [i for i in range(0,4)]
        items = self.generateItems(gamers)
        common.game.Game.__init__(self, field=field, items=items, gamers=gamers)
        
    def generateField(self):
        return Field(places={Coord(x,y): self.generatePlace(Coord(x,y))
            for x in range(0,self.size) 
            for y in range(0,self.size)
            })

    def generatePlace(self, coord: Coord):
        placeType = self.getPlaceType(coord)
        tile = None
        if (placeType == "GROUND"):
            tile=Tile()
        return Place(
                placeType=placeType,
                tile=tile
            )

    def getPlaceType(self, coord: Coord):
        m = self.size // 2
        (dx, dy) = (distance(m, coord.x), distance(m, coord.y))
        if dx > m or dy > m or (dx == m and dy == m):
            return 'EXCLUDED'
        if dx == m or dy == m or (dx == m-1 and dy == m-1):
            return 'SEA'
        return 'GROUND'

    def generateItems(self, gamers):
        items = []
        for gamer in gamers:
            items += [Item(gamer=gamer) for _ in range(0,4)]
        return items