import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d

X, Y = 0, 1
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def flipy(y):
	# converts chipmunk physics to pygame coordinates
	return -y + 600