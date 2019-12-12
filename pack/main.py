from random import shuffle


def listGenerator(items: list = [1, 2]):
    n = 0
    while n < len(items):
        yield items[n]
        n += 1


class Pack(object):
    def __init__(
        self,
        generator=listGenerator,
        reuseable: bool = False,
    ):
        self._generator = generator
        self._reuseable = reuseable
        self.items = []
        self.dropped = []

    def next(self):
        if len(self.items):
            try:
                item, *self.items = self.items
            except ValueError:
                item = None
        else:
            try:
                item = next(self._generator)
            except StopIteration:
                item = None
        if item is not None:
            if self._reuseable:
                self.dropped.append(item)
            return item
        if self._reuseable and (len(self.dropped) + len(self.items)):
            return self.reload().shuffle().next()
        return None

    def reload(self):
        if len(self.dropped) + len(self.items):
            self.items, self.dropped = self.items + self.dropped, []
        else:
            return None
        return self

    def shuffle(self):
        if self.items:
            shuffle(self.items)
        return self
