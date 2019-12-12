import tiles.tile
import random


class Generator(object):
    def next(self):
        return tiles.tile.Tile()


class TilesPack(object):
    def __init__(
        self,
        generator: Generator = Generator(),
        reusable: bool = False,
    ):
        self._reusable = reusable
        self._generator = generator
        self.items = []
        self.dropping = []

    def next(self):
        item = self._generator.next()
        if item:
            self.items.append(item)
            return item
        if self.reusable:
            self.reload()
            return self._generator.next()

    def reload(self):
        if len(self.dropping) + len(self.items):
            self.items, self.dropping = self.items + self.dropping, []
        else:
            return None
        return self

    def next(self):
        if len(self.items):
            item, *self.items = self.items
            return item
        return None

    def shuffle(self):
        if self.items:
            random.shuffle(self.items)
        return self