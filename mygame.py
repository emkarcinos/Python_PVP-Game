# import all files
from config import *
from sprites import Player, all_sprites, load_img, screen, HPBar, load_img_noalpha
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

# init resources

bg=load_img_noalpha("bg.png")
splash=load_img_noalpha("splash.png")
end=load_img_noalpha("end0.png")
p2end=load_img_noalpha("endp1.png")
p1end=load_img_noalpha("endp2.png")

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

def init_round():
    events.players.append(Player('p1', 400, 100, 10))
    events.players.append(Player('p2', 430, 300, 10))
    events.p1_group.add(events.players[0])
    events.p2_group.add(events.players[1])
    all_sprites.add(events.players)
    events.running=True
    events.bars.append(HPBar(200,886))
    events.bars.append(HPBar(570,886))
    all_sprites.add(events.bars)

def clear_round():
    events.players[0].delete()
    events.players[1].delete()
    for i in events.p1_bullet:
        i.delete()
    for i in events.p2_bullet:
        i.delete()
    events.p1_group.remove()
    events.p2_group.remove()
    events.players.clear()
    for i in events.bars:
        i.delete()
    events.bars.clear()
    events.p1_bullet.clear()
    events.p2_bullet.clear()
    events.p1_bullet_group.remove()
    events.p2_bullet_group.remove()
    all_sprites.remove()

def waitforkey():
    waiting=True
    while waiting:
        clock.tick(FPS) 
        pygame.event.pump()
        events.event_handler()   
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            waiting=False
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

def startscreen():
    screen.blit(splash,(0,0)) 
    pygame.display.flip()
    waitforkey()

def endscreen():
    if events.players[0].hp<=0 and events.players[1].hp<=0: #both players dead
        screen.blit(end,(0,0))
    elif events.players[0].hp<=0:
        screen.blit(p1end,(0,0))
    elif events.players[1].hp<=0:
        screen.blit(p2end,(0,0))
    pygame.display.flip()
    waitforkey()

# game loop
firstrun=True
while events.mainloop:
    init_round()
    if firstrun:
        startscreen()
    pygame.event.clear()
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
        #draw_debug_text()
        all_sprites.draw(screen)
        pygame.display.flip()   
    endscreen()
    clear_round()
    firstrun=False
pygame.quit()
sys.exit()