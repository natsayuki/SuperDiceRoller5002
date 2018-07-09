from random import randint

class Die:
    def __init__(self, min, max, name):
        self.min = min
        self.max = max
        self.name = name
        self.viewName = name.replace("Weighted ", '')
    def roll(self):
        return randint(self.min, self.max)
