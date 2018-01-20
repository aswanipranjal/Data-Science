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

	# keep ball velocity at a constant value
	def constant_velocity(body, gravity, damping, dt):
		body.velocity = body.velocity.normalized() * 400
	ball_body.velocity_func = constant_velocity
	space.add(ball_body, ball_shape)

def setup_level(space, player_body):
	# removes balls and bricks (all dynamic objects except the player body)
	for s in space.shapes[:]:
		if s.body.body_type == pymunk.Body.DYNAMIC and s.body not in [player_body]:
			space.remove(s.body, s)

	spawn_ball(space, player_body.position + (0, 40), random.choice([(1, 10), (-1, 10)])) # spawn a ball
	
	# spawn bricks
	for x in range(0, 21):
		x = x * 20 + 100
		for y in range(0, 5):
			y = y * 10 + 400
			brick_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
			brick_body.position = x, y
			brick_shape = pymunk.Poly.create_box(brick_body, (20, 10))
			brick_shape.elasticity = 1.0
			brick_shape.color = THECOLORS['blue']
			brick_shape.group = 1
			brick_shape.collision_type = collision_types['brick']
			space.add(brick_body, brick_shape)