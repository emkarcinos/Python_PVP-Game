# import all files
from config import *
import maps
#import events
# import modules
import os, sys
import pygame
from pygame.locals import *
# resource handler

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def load_img(name):
    img_path=os.path.join('data\graphics', name)
    image=pygame.image.load(img_path).convert()
    colorkey=image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_img_noalpha(name):
    img_path=os.path.join('data\graphics', name)
    image=pygame.image.load(img_path).convert()
    return image

def load_sound(name):
    sound_path=os.path.join('data\sounds')
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
        self.rect.center=vec(s_pos_x, s_pos_y)
        self.pos=vec(s_pos_x, s_pos_y)
        self.speed=vec(0, 0)
        self.acc=vec(0, 0)
        self.friction=-0.25
        self.facing=0     # where the player is looking (0-north, 1-east, 2-south, 3-west)
        self.colliding=False
        self.lastpos=(0,0)
        self.hp=PLAYER_HP
        self.alive=True
        self.hp_visible=False

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

    def wallcollide(self):
        for wall in maps.walls:
            if self.rect.colliderect(wall.rect):
                return True
        return False

    def gothit(self):
        self.hp_visible=True
        if self.hp>0:
            self.hp-=BULLET_DMG
        if self.hp<=0:
            self.alive=False
        
    def move(self):
        if self.colliding or self.wallcollide():
            self.rect.center=self.lastpos
            self.pos=vec(self.lastpos[0], self.lastpos[1])  ## tuple to vector
            self.speed=vec(0, 0)
            self.acc=vec(0, 0)
            self.colliding=False
        else:
            self.lastpos=self.rect.center
            self.acc+=self.speed*self.friction
            self.speed+=self.acc
            self.pos+=self.speed+0.5*self.acc
            self.rect.center=self.pos

    def update(self):
        self.move()

    def delete(self):
        self.kill()
    
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
        if not pygame.sprite.spritecollideany(self, maps.bwalls, collided = None)==None:
            self.kill()
    
    def delete(self):
        self.kill()

class HPBar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((150, 30))
        self.image.fill((87,156,135))
        self.rect=self.image.get_rect()
        self.rect.center=((x, y))
        self.width=150

    def gothit(self):
        self.width-=int(150*(BULLET_DMG/100))
        self.width=max([self.width, 0])
        self.image=pygame.transform.scale(self.image, (self.width, 30))

    def update(self):
        self.gothit
        
    def delete(self):
        self.kill()