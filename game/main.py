import common.game
from common.field import Field, Place
from common.coordinates import Coord

class Game(common.game.Game):
    def __init__(self):
        field = Field(places={Coord(x,y): Place() for x in range(0,13) for y in range(0,13)})
        items = []
        gamers = [i for i in range(0,3)]
        common.game.Game.__init__(self, field=field, items=items, gamers=gamers)
        
