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

	# bricks should be removed when hit by the ball
	def remove_brick(arbiter, space, data):
		brick_shape = arbiter.shapes[0]
		space.remove(brick_shape, brick_shape.body)

	# add collision handler
	h = space.add_collision_handler(collision_types['brick'], collision_types['ball'])
	h.separate = remove_brick

def main():
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()
	running = True
	font = pygame.font.SysFont('Arial', 16)

	space = pymunk.Space()
	draw_options = pymunk.pygame_util.DrawOptions(screen)

	# walls
	static_lines = [pymunk.Segment(space.static_body, (50, 50), (50, 550), 2),
					pymunk.Segment(space.static_body, (50, 550), (550, 550), 2),
					pymunk.Segment(space.static_body, (550, 550), (550, 50), 2)]
	for line in static_lines:
		line.color = THECOLORS['lightgray']
		line.elasticity = 1.0

	space.add(static_lines)

	# bottom sensor
	bottom = pymunk.Segment(space.static_body, (50, 50), (550, 50), 2)
	bottom.sensor = True
	bottom.collision_type = collision_types['bottom']
	bottom.color = THECOLORS['red']
	def remove_first(arbiter, space, data):
		ball_shape = arbiter.shapes[0]
		space.remove(ball_shape, ball_shape.body)
		return True

	h = space.add_collision_handler(collision_types['ball'], collision_types['bottom'])
	h.begin = remove_first
	space.add(bottom)

	# player
	player_body = pm.Body(500, pymunk.inf)
	player_body.position = 300, 100

	player_shape = pymunk.Segment(player_body, (-50, 0), (50, 0), 8)
	player_shape.color = THECOLORS['red']
	player_shape.elasticity = 1.0
	player_shape.collision_type = collision_types['player']

	def pre_solve(arbiter, space, data):
		set_ = arbiter.contact_point_set
		if len(set_.points) > 0:
			player_shape = arbiter.shapes[0]
			width = (player_shape.b - player_shape.a).x
			delta = (player_shape.body.position - set_.points[0].point_a.x).x
			normal = Vec2d(0, 1).rotated(delta / width / 2)
			set_.normal = normal
			set_.points[0].distance = 0
		arbiter.contact_point_set = set_
		return True
	h = space.add_collision_handler(collision_types['player'], collision_types['ball'])
	h.pre_solve = pre_solve