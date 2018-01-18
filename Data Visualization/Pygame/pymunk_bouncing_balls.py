import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
import random
import math
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

space = pygame.Space()
space.gravity = (0.0, -900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

balls = []

static_body = space.static_body
static_lines = [pymunk.Segment(static_body, (111.0, 280.0), (407.0, 246.0), 0.0),
				pymunk.Segment(static_body, (407.0, 246.0), (407.0, 343.0), 0.0)]

for line in static_lines:
	line.elasticity = 0.95
	line.friction = 0.9
space.add(static_lines)

ticks_next_to_ball = 10
