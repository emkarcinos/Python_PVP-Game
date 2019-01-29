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

events.players.append(Player('asd', 400, 100, 10))
events.players.append(Player('qwe', 400, 500, 10))
events.p1_group.add(events.players[0])
events.p2_group.add(events.players[1])
all_sprites.add(events.players)

events.running=True

# debug text

font=pygame.font.SysFont("Arial", 12)

def draw_debug_text():
    texts=[
            font.render("P1 facing: " + str(events.players[0].facing), True, (100,100,100)),
            font.render("P2 facing: " + str(events.players[1].facing), True, (100,100,100)),
            font.render("P1 bullets: " + str(len(events.p1_bullet)), True, (100,100,100)),
            font.render("P2 bullets: " + str(len(events.p2_bullet)), True, (100,100,100))
        ]
    count=0
    for text in texts:
        screen.blit(text, (0,count*12))
        count+=1

# set hitbox objects as screen boundaries ### DEBUG ###
boundary=pygame.sprite.Group()
boundary.add=Hitbox(int(WINDOW_WIDTH/2), 0, WINDOW_WIDTH, 10)

bg, bg_rect=load_img("bg.png")
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
    screen.blit(bg,(0,0))
    draw_debug_text()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()