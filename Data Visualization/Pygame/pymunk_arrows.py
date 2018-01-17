import sys

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

def create_arrow():
	vs = [(-30, 0), (0, 3), (10, 0), (0, -3)]
	mass = 1
	moment = pymunk.moment_for_poly(mass, vs)
	arrow_body = pymunk.Body(mass, moment)

	arrow_shape = pymunk.Poly(arrow_body, vs)
	arrow_shape.friction = .5
	arrow_shape.collision_type = 1
	