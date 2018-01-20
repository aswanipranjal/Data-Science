import random

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

space = pymunk.Space()
space.gravity = (0.0, -900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

balls = []

static_lines = [pymunk.Segment(space.static_body, (150.0, 100.0), ( 50.0, 550.0), 1.0),
				pymunk.Segment(space.static_body, (450.0, 100.0), (550.0, 550.0), 1.0),
				pymunk.Segment(space.static_body, ( 50.0, 550.0), (300.0, 600.0), 1.0),
				pymunk.Segment(space.static_body, (300.0, 600.0), (550.0, 550.0), 1.0),
				pymunk.Segment(space.static_body, (300.0, 420.0), (400.0, 400.0), 1.0)]
for line in static_lines:
	line.elasticity = 0.7
	line.group = 1
space.add(static_lines)

fp = [(20, -20), (-120, 0), (20, 20)]
mass = 100
moment = pymunk.moment_for_poly(mass, fp)

# right flipper
r_flipper_body = pymunk.Body(mass, moment)
r_flipper_body.position = 450, 100
r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
space.add(r_flipper_body, r_flipper_shape)

r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_flipper_joint_body.position = r_flipper_body.position
j = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0, 0), (0, 0))
s = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.15, 20000000, 900000)
space.add(j, s)