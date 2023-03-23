import pygame as pg
from random import randint

class Figur:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class Hinder(Figur):
    def __init__(self, x, y, fartY):
        super().__init__(x, y)
        self._fartY = fartY
    
    def tegn(self, vindu):
        pg.draw.rect(vindu, (3,67,86), (self._x, self._y, self._bredde, self._hoyde))

class Spiller(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self._fartX = fartX

    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._x, self._y), 25)