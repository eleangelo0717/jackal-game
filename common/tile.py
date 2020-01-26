class Tile(object):
    def __init__(self, angle=0, opened=False):
        self.angle = angle
        self._opened = opened

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def getClassName(self):
        return self.__class__.__name__

    def onOpen(self, game):
        print('Open', self, game)
        return

    def onAction(self):
        return

    def open(self):
        self._opened = True

    def isOpened(self):
        return self._opened

    def to_json(self):
        result = {
            'type': self.getClassName()
        }
        return result
