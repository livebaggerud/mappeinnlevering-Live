import pygame as pg
from ball import Ball
from hinder import Hinder
import time

spiller1 = Ball()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init()
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])


forsett = True
while forsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            forsett = False
    
    vindu.fill((255,255,255)) #farger bakrunnen hvit
    #vindu.fill((rød, grønn, blå)) 0-255
    
    spiller1.tegn(vindu)
    #pg.draw.circle(vindu, (rød, grønn, blå), (x, y), radius)
    
    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)
    
    #pg.draw.rect(vindu, (rød, grønn, blå), (x, y, bredde, høyde))

    pg.display.flip()
    time.sleep(0.1)

pg.quit()

    

print("ferdig")

        