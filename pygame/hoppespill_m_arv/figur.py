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
        self._hoyde = randint(50,120)
        self._y = 720 - self._hoyde
        self._bredde = 25
    
    def tegn(self, vindu):
        pg.draw.rect(vindu, (3,67,86), (self._x, self._y, self._bredde, self._hoyde))

    def flytt_venstre(self):
        self._x -= 1

class Spiller(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self._fartX = fartX
        self._radius = 25

    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (self._x, self._y), self._radius)

    def hopp(self):
        self._y -= 5

    def fall(self):
        if self._y < 720 - self._radius:
            self._y += 0.5

    def er_over_hinder(self):
        pass



pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
spiller = Spiller(30, 650, 50)
hindere = []

for i in range(100):
    nytt_hinder = Hinder(1200,650,90)
    hindere.append(nytt_hinder)

frame = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if frame == 400:
        frame = 0
        nytt_hinder = Hinder(1200, 650, 300)
        hindere.append(nytt_hinder)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    spiller.tegn(screen)

    for hinder in hindere:
        hinder.tegn(screen)
        hinder.flytt_venstre()
        

    
    

    # LAG SPILLET DIT HER:

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        spiller.hopp()
    
    spiller.fall()
    
    frame += 1
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()
