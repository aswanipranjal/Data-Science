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

def mouse_coll_func(arbiter, space, data):
	# simple callback to increase the radius of circles touching the mouse
	s1, s2 = arbiter.shapes
	s2.unsafe_set_radius(s2.radius + 0.15)
	return False

	