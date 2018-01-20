import sys
import random
import pygame
from pygame.locals import *

import pymunk
import pymunk.pygame_util

def add_ball(space):
	mass = 1
	radius = 14
	inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
	body = pymunk.Body(mass, inertia)
	x = random.randint(120, 380)
	body.position = x, 550
	shape = pymunk.Circle(body, radius, (0, 0))
	space.add(body, shape)
	return shape
