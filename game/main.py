import common.game
from common.field import Field, Place
from common.coordinates import Coord
from common.utils import distance
from common.tile import Tile
from game.items import Ship, Pirate, Coin

FIELD_SIZE = 13
GAMERS = 4
PIRATES = 3

class Game(common.game.Game):
    def __init__(self):
        self.size = FIELD_SIZE
        self.middle = FIELD_SIZE // 2
        field = self.generateField()
        gamers = [i for i in range(0, GAMERS)]
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
        (dx, dy) = (distance(self.middle, coord.x), distance(self.middle, coord.y))
        if dx > self.middle or dy > self.middle or (dx == self.middle and dy == self.middle):
            return 'EXCLUDED'
        if dx == self.middle or dy == self.middle or (dx == self.middle-1 and dy == self.middle-1):
            return 'SEA'
        return 'GROUND'

    def generateItems(self, gamers):
        items = []
        for gamer in gamers:
            items += [Ship(gamer=gamer, coordinates=self.getStartCoord(gamer)) for _ in range(0, 1)]
            items += [Pirate(gamer=gamer, coordinates=self.getStartCoord(gamer)) for _ in range(0, PIRATES)]
        return {i: val for i, val in enumerate(items)}

    def getStartCoord(self, gamer):
        places = [
            Coord(self.middle,0),
            Coord(0,self.middle),
            Coord(self.middle,self.size-1),
            Coord(self.size-1, self.middle)
        ]
        return places[gamer % GAMERS]