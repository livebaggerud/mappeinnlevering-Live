import pygame as pg

class Ball:
    def __init__(self):
        self._posx = 20
        self._posy = 20

    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._posx, self._posy), 25)