from tiles import TilesPack


class FieldPlace(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opened = False
        self.isExisits = self.__isExists()
        self.isGround = self.__isGround()
        self.tile = None

    def __repr__(self):
        if self.isExisits:
            return f"<{self.__class__.__name__} [{self.x}:{self.y}] Tile:{self.tile}>"
        else:
            return f"<{self.__class__.__name__}>"

    def __isExists(self):
        return not ((self.x == 0 or self.x == 12) and (self.y == 0 or self.y == 12))

    def __isGround(self):
        return self.__isExists() and (
            not (
                (self.x == 0 or self.x == 12 or self.y == 0 or self.y == 12) or (
                    (self.x == 1 or self.x == 11) and (
                        self.y == 1 or self.y == 11)
                )
            )
        )

    def Open(self):
        if self.isExisits and self.tile and not self.opened:
            self.opened = True
            return self.tile
        return None

    def View(self):
        if self.isExisits and self.tile and self.opened:
            return self.tile
        return None


class Field(object):

    def __init__(self):
        self.places = [[FieldPlace(row, col)
                        for col in range(13)] for row in range(13)]
        self.__placeTiles()

    def __placeTiles(self):
        tilesPack = TilesPack()
        for row in self.places:
            for place in row:
                if place.isGround:
                    place.tile = tilesPack.Next()

    def getPlace(self, x, y):
        try:
            return self.places[x][y] 
        except:
            return None
        return None

    def getNeighboringPlaces(self, place, moveArray):
        if not place.isExisits:
            return []
        return [p for p in [
            self.getPlace(place.x + m[0], place.y + m[1]) 
            for m in moveArray 
            if place.x + m[0] >=0 and place.y + m[1] >= 0
            ] if p]

    def isPlaceGround(self, x, y):
        if not self.isPlaceInField(x, y):
            return False
        return self.places[x][y].isGround    

    def isPlaceOcean(self, x, y):
        if not self.isPlaceInField(x, y):
            return False
        return not self.places[x][y].isGround      

    def isPlaceInField(self, x, y):
        return len(self.places) and x >= 0 and y >= 0 and x < len(self.places) and y < len(self.places[0]) and self.places[x][y].isExisits

    def isPlaceNearChest(self, x, y):
        if not self.isPlaceInField(x, y):
            return False
        for dx in [1, -1]:
            if self.isPlaceGround(x + dx, y):
                return True
        for dy in [1, -1]:
            if self.isPlaceGround(x, y + dy):
                return True
        return False
