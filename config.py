# Config variables
import pygame
from pygame.locals import *

# Runtime settings
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 1000
FPS = 30
WIN_NAME = "Kostschevsky's shooter"

PLAYER_HP=100

# Controls

# player 1
P1_UP=pygame.K_w
P1_DOWN=pygame.K_s
P1_RIGHT=pygame.K_d
P1_LEFT=pygame.K_a
P1_SHOOT=pygame.K_LCTRL

# player 2
P2_UP=pygame.K_UP
P2_DOWN=pygame.K_DOWN
P2_RIGHT=pygame.K_RIGHT
P2_LEFT=pygame.K_LEFT
P2_SHOOT=pygame.K_RCTRL

# bullets
BULLET_SPEED=20
SHOOT_SPEED=200
BULLET_DMG=20
