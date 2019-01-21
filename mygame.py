# import all files
from config import *
from sprites import *
from colours import *
import events
# import modules
import os, sys
import pygame
from pygame.locals import *

# JEChANE

# initialization

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WIN_NAME)
clock=pygame.time.Clock()

# initialize two players

events.players.append(Player('asd', 400, 100, 5))
events.players.append(Player('qwe', 400, 500, 5))
all_sprites.add(events.players)

events.running=True

# game loop

while events.running:
    clock.tick(FPS)
    # events
    pygame.event.pump()
    events.event_handler()
    # update
    all_sprites.update()
    screen.fill(BLACK)
    # draw
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit() 
sys.exit()