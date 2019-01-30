# import all files
from config import *
from sprites import Player, all_sprites, load_img, screen
from colours import *
import maps 
import events
# import modules
from os import path
import os, sys
import pygame
from pygame.locals import *

# initialization

pygame.init()
#pygame.mixer.init()
pygame.display.set_caption(WIN_NAME)
clock=pygame.time.Clock()

# initialize two players

events.players.append(Player('p1', 400, 100, 10))
events.players.append(Player('p2', 430, 300, 10))
events.p1_group.add(events.players[0])
events.p2_group.add(events.players[1])
all_sprites.add(events.players)
events.running=True

# debug text

font=pygame.font.SysFont("Arial", 12)

def draw_debug_text():
    texts=[
            font.render("P1 HP: " + str(events.players[0].hp), True, (100,100,100)),
            font.render("P2 HP: " + str(events.players[1].hp), True, (100,100,100))
        ]
    count=0
    for text in texts:
        screen.blit(text, (0,count*12))
        count+=1

bg, bg_rect=load_img("bg.png")

def startscreen():
    screen.fill(BGCOLOR)

# game loop
while events.mainloop:
    print('asd')
    while events.running:
        clock.tick(FPS)
        # events
        pygame.event.pump()
        events.event_handler()
        # update
        all_sprites.update()
        screen.fill(BLACK)
        if events.dead():
            break
        # draw
        screen.blit(bg,(0,0))
        draw_debug_text()
        all_sprites.draw(screen)
        pygame.display.flip()
    print('asd')
pygame.quit()
sys.exit()