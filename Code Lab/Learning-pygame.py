import pygame as pg
pg.init()
screen=pg.display.set_mode((500,500))
running=True
while running:
    screen.fill((255,0,0))
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
