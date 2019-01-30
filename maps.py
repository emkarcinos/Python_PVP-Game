from os import path
import pygame

walls=pygame.sprite.Group()
bwalls=pygame.sprite.Group()

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, x, y, instance):
        if instance=='player':
            self.groups=walls
        elif instance=='bullet':
            self.groups=bwalls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image=pygame.Surface((20,20))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=x*20
        self.rect.y=y*20

game_folder=path.dirname(__file__)
map_pdata=[]
map_bdata=[]

# player collison map

with open(path.join(game_folder, 'map_player_collision.txt')) as f:
    for line in f:
        map_pdata.append(line)
        
for row, tiles in enumerate(map_pdata):
    for col, tile in enumerate(tiles):
        if tile=='1':
            Hitbox(col, row, 'player')

# bullet collision map

with open(path.join(game_folder, 'map_bullet_collision.txt')) as f:
    for line in f:
        map_bdata.append(line)
        
for row, tiles in enumerate(map_bdata):
    for col, tile in enumerate(tiles):
        if tile=='1':
            Hitbox(col, row, 'bullet')

