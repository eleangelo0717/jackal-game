import random


class Generator(object):
    def next(self):
        return 0


class Pack(object):
    def __init__(
        self,
        generator: Generator = Generator(),
        reuseable: bool = False,
    ):
        self._generator = generator
        self._reuseable = reuseable
        self.items = []
        self.dropping = []

    def next(self):
        item = self._generator.next()
        if item:
            if self._reuseable:
                self.items.append(item)
            return item
        if self._reuseable and (len(self.dropping) + len(self.items)):
            return self.reload().shuffle().next()
        return None

    def reload(self):
        if len(self.dropping) + len(self.items):
            self.items, self.dropping = self.items + self.dropping, []
        else:
            return None
        return self

    def shuffle(self):
        if self.items:
            random.shuffle(self.items)
        return self
