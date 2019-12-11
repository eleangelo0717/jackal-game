from tiles import TilesPack
import moves

class FieldPlace(object):

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.opened = False
        self._exisits = self._isExists()
        self._ground = self._isGround()
        self.tile = None

    def __repr__(self):
        if self._exisits:
            return f"<{self.__class__.__name__} [{self.x}:{self.y}] Tile:{self.tile}>"
        else:
            return f"<{self.__class__.__name__}>"

    def _isExists(self):
        return not ((self.x == 0 or self.x == 12) and (self.y == 0 or self.y == 12))

    def _isGround(self):
        return self._exisits and (
            not (
                (self.x == 0 or self.x == 12 or self.y == 0 or self.y == 12) or (
                    (self.x == 1 or self.x == 11) and (
                        self.y == 1 or self.y == 11)
                )
            )
        )


    def getPlaceByDirection(self, direction):
        (x, y) = (self.x + direction.x, self.y + direction.y)
        if x < 0 or y < 0:
            return None
        return self.field.getPlaceByCoordinates(x, y)
        

    def getNeighboringPlaces(self, moveArray=moves.directions4):
        if not self.isExists():
            return []
        return [p for p in [
            self.getPlaceByDirection(direction)
            for direction in moveArray 
            ] if p]

    def isExists(self):
        return self._exisits

    def isGround(self):
        return self._exisits and self._ground
    
    def isSea(self):
        return self._exisits and not self._ground

    def open(self):
        if self.isGround() and self.tile and not self.opened:
            self.opened = True
            return self.tile
        return None

    def view(self):
        if self.isGround() and self.tile and self.opened:
            return self.tile
        return None

    def hasTeamShip(self, team):
        for i in self.field.game.items:
            if i.x == self.x and i.y == self.y and i.gamer.team == team:
                return True
        return False

    def getItems(self):
        return [item for item in self.field.game.items if item.x == self.x and item.y == self.y]

    def placeTile(self, tile):
        self.tile = tile
        tile.place = self

class Field(object):

    def __init__(self, game):
        self.game = game
        self.places = [[FieldPlace(self, row, col)
                        for col in range(13)] for row in range(13)]
        self._placeTiles()

    def _placeTiles(self):
        tilesPack = TilesPack()
        for row in self.places:
            for place in row:
                if place.isGround():
                    place.tile = tilesPack.Next()
                    place.tile.place = place

    def getPlaceByCoordinates(self, x, y):
        place = None
        try:
            place = self.places[x][y] 
        except:
            return None
        if place.isExists():
            return place
        return None
