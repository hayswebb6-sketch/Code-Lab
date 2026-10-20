import pygame as pg
pg.init()
pg.mouse.set_visible(False)
screen=pg.display.set_mode((0,0), pg.FULLSCREEN)
vsync_switch_on=False
vsync_switch_x=100.0
running=True
x=50
y=50
while running:
    screen.fill((0,0,0))
    pg.draw.rect(screen,(0,255,0),(x,y,100,100))
    pg.draw.rect(screen, (46,180,100) if vsync_switch_on else (65,65,75), (100, 100, 60, 30), border_radius=15)
    pg.draw.circle(screen,(255,255,255),(int(vsync_switch_x),115,),11)
    vsync_switch_x+=((139 if vsync_switch_on else 121)-vsync_switch_x)*0.2
    pg.display.flip()
    keys=pg.key.get_pressed()
    movement=pg.math.Vector2(0,0)
    if keys[pg.K_a]:
        movement.x-=1
    if keys[pg.K_d]:
        movement.x+=1
    if keys[pg.K_s]:
        movement.y+=1
    if keys[pg.K_w]:
        movement.y-=1
    if keys[pg.K_ESCAPE]:
        pg.mouse.set_visible(True)
    if movement.length()>0:
        movement=movement.normalize()
        x+=movement.x
        y+=movement.y
    if vsync_switch_on==True:
        pg.time.Clock().tick(60)
    else:
        pg.time.Clock().tick(0)
    
    for event in pg.event.get():
        if event.type==pg.MOUSEBUTTONDOWN:
            if pg.Rect(100,100,60,30).collidepoint(event.pos):
                vsync_switch_on= not vsync_switch_on
        if event.type==pg.QUIT:
            running=False
