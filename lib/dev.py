from .freebie import Freebie


class Dev:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def freebies(self):
        return [fb for fb in Freebie.all if fb.dev == self]

    @property
    def companies(self):
        return [fb.company for fb in self.freebies]
