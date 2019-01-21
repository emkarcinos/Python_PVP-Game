import os, sys
import pygame
from pygame.locals import *

from sprites import *

running=True
players=[]

def events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

def collision_check(p):
    # collision between players
    if players[0].rect.colliderect(players[1].rect): 
        if p==1:
            players[0].colliding=True
            direction=players[1].facing
            players[0].facing=(direction+2)%4
            return True
        elif p==0:
            players[1].colliding=True
            direction=players[0].facing
            players[1].facing=(direction+2)%4
            return True
        else:
            players[0].colliding=True
            players[1].colliding=True

    else:
        return False

def player1_input(keys):
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

def event_handler():
    events()
    keys=pygame.key.get_pressed()
    collision_check(-1)
    player1_input(keys)
    player2_input(keys) 
    
    