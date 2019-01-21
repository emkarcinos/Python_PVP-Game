# import all files
from config import *
import events
# import modules
import os, sys
import pygame
from pygame.locals import *

# resource handler

def load_img(name):
    img_path=os.path.join('data/graphics', name)
    image=pygame.image.load(img_path).convert()
    colorkey=image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    sound_path=os.path.join('data\\sounds')
    sound=pygame.mixer.Sound(sound_path)
    return sound

# sprite groups

all_sprites=pygame.sprite.Group()

# sprites classes

vec=pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, fname, s_pos_x, s_pos_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect=load_img(fname +'.png')
        self.rect.center=(s_pos_x, s_pos_y)
        self.pos=vec(s_pos_x, s_pos_y)
        self.speed=vec(0, 0)
        self.acc=vec(0, 0)
        self.friction=-0.25
        self.facing=0     # where the player is looking (0-north, 1-east, 2-south, 3-west)
        self.colliding=False

    def moveup(self):
        self.facing=0
        self.acc.y=-1.5
        self.acc.x=0

    def movedown(self):
        self.facing=2
        self.acc.y=1.5
        self.acc.x=0

    def moveright(self):
        self.facing=1
        self.acc.x=1.5
        self.acc.y=0

    def moveleft(self):
        self.facing=3
        self.acc.x=-1.5
        self.acc.y=0
    
    def stopmoving(self):
        self.acc=vec(0, 0)

    def move(self):
        if self.colliding:
            if self.facing==0:
                self.pos.y+=1
            elif self.facing==1:
                self.pos.x-=1
            elif self.facing==2:
                self.pos.y-=1
            elif self.facing==3:
                self.pos.x+=1   
            self.rect.center=self.pos
            self.speed=vec(0, 0)
            self.acc=vec(0, 0)
            self.colliding=False
        else:
            self.acc+=self.speed*self.friction
            self.speed+=self.acc
            self.pos+=self.speed+0.5*self.acc
            self.rect.center=self.pos

    def update(self):
        self.move()     

class Bullet(pygame.sprite.Sprite):
    def __init__(self, fname):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect=load_img(fname + '.png')

