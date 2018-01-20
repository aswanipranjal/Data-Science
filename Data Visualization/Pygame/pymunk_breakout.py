import os
import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

width, height = 600, 600

collision_types = {
	'ball': 1,
	'brick': 2,
	'bottom': 3,
	'player': 4,
}

def spawn_ball(space, position, direction):
	ball_body = pymunk.Body(1, pymunk.inf)
	ball_body.position = position

	ball_shape = pymunk.Circle(ball_body, 5)
	ball_shape.color = THECOLORS['green']
	ball_shape.elasticity = 1.0
	ball_shape.collision_type = collision_types['ball']

	ball_body.apply_impulse_at_local_point(Vec2d(direction))