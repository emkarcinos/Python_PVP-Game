# import all files
from config import *
#import events
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
    sound_path=os.path.join('data/sounds')
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
        if self.facing!=0:
            self.image=pygame.transform.rotate(self.image, (self.facing*90))
        self.facing=0
        self.acc.y=-1.5
        self.acc.x=0

    def movedown(self):
        if self.facing!=2:
            self.image=pygame.transform.rotate(self.image, (self.facing*90)-180)
        self.facing=2
        self.acc.y=1.5
        self.acc.x=0

    def moveright(self):
        if self.facing!=1:
            self.image=pygame.transform.rotate(self.image, (self.facing*90)-90)
        self.facing=1
        self.acc.x=1.5
        self.acc.y=0

    def moveleft(self):
        if self.facing!=3:
            self.image=pygame.transform.rotate(self.image, (self.facing*90)-270)
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
    def __init__(self, fname, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect=load_img(fname + '.png')
        self.rect.center=(x, y)
        self.speed=vec(0, 0)
        self.direction=direction
    
    def shoot(self):
        if self.direction==0:
            self.speed.y=-BULLET_SPEED
        elif self.direction==1:
           self.speed.x=BULLET_SPEED
        elif self.direction==2:
            self.speed.y=BULLET_SPEED
        elif self.direction==3:
            self.speed.x=-BULLET_SPEED
        self.rect.center+=self.speed

    def update(self):
        self.shoot()

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        self.size=vec(w, h)
        self.rect=self.size.get_rect()
        self.rect.center=vec(x,y)