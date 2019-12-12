import actions.tile
import actions.game


class Tile(object):
    def __init__(self, angle=0, opened=False):
        self.angle = angle
        self._opened = opened

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def className(self):
        return self.__class__.__name__

    def onOpen(self):
        return actions.tile.open

    def onAction(self):
        return actions.game.passageTransition

    def open(self):
        self._opened = True

    def isOpened(self):
        return self._opened

