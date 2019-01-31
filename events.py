import os, sys
import pygame
from pygame.locals import *

from sprites import *
from config import *

mainloop=True
running=True
players=[]

p1_group=pygame.sprite.Group()
p2_group=pygame.sprite.Group()
p1_bullet=[]
p2_bullet=[]

p1_bullet_group=pygame.sprite.Group()
p2_bullet_group=pygame.sprite.Group()

clock=pygame.time.Clock()
clock.tick()
timer1=1000
clock2=pygame.time.Clock()
clock2.tick()
timer2=1000

bars=[]

def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #running=False

def collision_check(p):
    # collision between players
    if players[0].rect.colliderect(players[1].rect): 
        if p==1:
            players[0].colliding=True
            direction=players[1].facing
            players[0].image=pygame.transform.rotate(players[0].image, players[0].facing*90-((direction+2)%4)*90)
            players[0].facing=(direction+2)%4
            return True
        elif p==0:
            players[1].colliding=True
            direction=players[0].facing
            players[1].image=pygame.transform.rotate(players[1].image, players[1].facing*90-((direction+2)%4)*90)
            players[1].facing=(direction+2)%4
            return True
        else:
            players[0].colliding=True
            players[1].colliding=True

    else:
        return False

def bullethits():
    hits1=pygame.sprite.groupcollide(p2_group, p1_bullet_group, False, True)
    hits2=pygame.sprite.groupcollide(p1_group, p2_bullet_group, False, True)
    if hits1:
        players[1].gothit()
        bars[1].gothit()
    if hits2:
        players[0].gothit()
        bars[0].gothit()

def player1_input(keys):
    if keys[P1_SHOOT]:
        global timer1
        p1_bullet.append(Bullet('bullet', players[0].pos.x, players[0].pos.y, players[0].facing))
        if timer1>SHOOT_SPEED:
            p1_bullet_group.add(p1_bullet[-1])
            all_sprites.add(p1_bullet[-1])
            p1_bullet[-1].direction=players[0].facing
            p1_bullet[-1].shoot()
            timer1=clock.tick()
        else:
            del p1_bullet[-1]
    if not (keys[P1_UP] or keys[P1_DOWN] or keys[P1_RIGHT] or keys[P1_LEFT]):
        players[0].stopmoving()
    elif not collision_check(0):
        if keys[P1_RIGHT]:
            players[0].moveright()
        if keys[P1_LEFT]:
            players[0].moveleft()
        if keys[P1_UP]:
            players[0].moveup()
        if keys[P1_DOWN]:
            players[0].movedown()

def player2_input(keys):
    if keys[P2_SHOOT]:
        global timer2
        p2_bullet.append(Bullet('bullet', players[1].pos.x, players[1].pos.y, players[1].facing))
        if timer2>SHOOT_SPEED:
            p2_bullet_group.add(p2_bullet[-1])
            all_sprites.add(p2_bullet[-1])
            p2_bullet[-1].direction=players[1].facing
            p2_bullet[-1].shoot()
            timer2=clock.tick()
        else:
            del p2_bullet[-1]
    if not (keys[P2_UP] or keys[P2_DOWN] or keys[P2_RIGHT] or keys[P2_LEFT]):
        players[1].stopmoving()
    elif not collision_check(1):
        if keys[P2_RIGHT]:
            players[1].moveright()
        if keys[P2_LEFT]:
            players[1].moveleft()
        if keys[P2_UP]:
            players[1].moveup()
        if keys[P2_DOWN]:
            players[1].movedown() 
def dead():
    if players[0].alive and players[1].alive:
        return False
    else:
        return True

def event_handler():
    global timer1
    global timer2
    events()
    keys=pygame.key.get_pressed()
    collision_check(-1)
    bullethits()
    timer1+=clock.tick()
    timer2+=clock2.tick()
    player1_input(keys)
    player2_input(keys) 
    
    