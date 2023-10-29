from .freebie import Freebie


class Company:
    all = []

    def __init__(self, name, fyear):
        self.name = name
        self.fyear = fyear
        type(self).all.append(self)

    @classmethod
    def oldest_company(cls):
        years = [co.fyear for co in cls.all]
        return next((co for co in cls.all if co.fyear == sorted(years)[0]), None)

    @property
    def freebies(self):
        return [fb for fb in Freebie.all if fb.company == self]

    @property
    def devs(self):
        return [fb.dev for fb in self.freebies]

    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name, value, dev, self)
