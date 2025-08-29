import random

class Dice:
    def __init__(self):
        self.__values__ = (0, 0)

    def roll(self):
        self.__values__ = (random.randint(1, 6), random.randint(1, 6))
        return self.__values__