from random import randint
import pygame as pg

class Hinder:
    def __init__(self):
        self._posx = 300
        self._hoyde = randint(20, 100)
        self._posy = 500 - self._hoyde
        self._bredde = 10

    def flytt_venstre(self):
        self._posx -= 1

    def tegn(self, vindu):
        pg.draw.rect(vindu, (3,67,86), (self._posx, self._posy, self._bredde, self._hoyde))