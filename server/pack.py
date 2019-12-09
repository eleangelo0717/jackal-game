import random

class Pack(object):
    def __init__(self, items):
        self.items = items
        self.Shuffle()

    def Shuffle(self):
        random.shuffle(self.items)

    def Next(self):
        if len(self.items) == 0:
            return None
        item, self.items = self.items[0], self.items[1:]
        return item

    