__docformat__ = "reStructuredText"

import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True

	space = pymunk.Space()
	draw_options = pymunk.pygame_util.DrawOptions(screen)

	pointer_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

	polygon_shape = [(80, 0), (0, 20), (0, -20)]
	moment = pymunk.moment_for_poly(1, polygon_shape)
	gun_body = pymunk.Body(1, moment)
	gun_body.position = 300, 300
	gun_shape = pymunk.Poyl(gun_body, polygon_shape)

	rest_angle = 0
	stiffness = 125000.
	damping = 6000.

	rotary_spring = pymunk.constraint.DampedRotarySpring(pointer_body, gun_body, rest_angle)
	space.add(gun_body, gun_shape, rotary_spring)