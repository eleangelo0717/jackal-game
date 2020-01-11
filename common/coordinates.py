from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Coord:
    x: int
    y: int

    def __repr__(self):
        return f'[{self.x}:{self.y}]'

    def rotate(self, angle=0):
        (x, y) = [
            (self.x, self.y),
            (self.y, -self.x),
            (-self.x, -self.y),
            (-self.y, self.x)
        ][angle]
        return Coord(x,y)

class DeltaCoord(Coord):
    def __repr__(self):
        fmt = '{:+d}'
        return f'({fmt.format(self.x)}:{fmt.format(self.y)})'  

class Move(object):
    def __init__(self, direction: DeltaCoord = None, start: Coord = None, destination: Coord = None):
        self.__destination = destination
        self.__start = start
        self.__direction = direction or DeltaCoord(0,0)
        self.__checkValues()

    def setStart(self, start: Coord = None):
        self.__start = start
        self.__checkValues()

    def setDirection(self, direction: DeltaCoord = None):
        self.__direction = direction
        if (self.__start):
            self.__destination = Coord(
                self.__start.x + self.__direction.x,
                self.__start.y + self.__direction.y)

    def getDestination(self): return self.__destination

    def setDestination(self, destination: Coord = None):
        self.__destination = destination
        if (self.__start):
            self.__direction = Coord(
                self.__destination.x - self.__start.x,
                self.__destination.y - self.__start.y)

    destination = property(getDestination, setDestination)

    def __checkValues(self):
        if (self.__start):
            if (self.__direction):
                self.__destination = Coord(
                    self.__start.x + self.__direction.x,
                    self.__start.y + self.__direction.y)
            elif (self.__destination):
                self.__direction = Coord(
                    self.__destination.x - self.__start.x,
                    self.__destination.y - self.__start.y)

    def __repr__(self):
        if (self.__start):
            return f"<{self.__class__.__name__} {self.__start}->{self.__destination}>"
        return f"<{self.__class__.__name__} {self.__direction}>"

