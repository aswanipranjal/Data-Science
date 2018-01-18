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

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True

	space = pymunk.Space()
	space.gravity = 0.0, -900.0

	balls = []

	mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
	mouse_shape.collision_type = COLLTYPE_MOUSE
	space.add(mouse_shape)
	space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL).pre_solve=mouse_coll_func

	# static line
	line_point1 = None
	static_lines = []
	run_physics = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'balls_and_lines.png')
			elif event.type == MOUSEBUBTTONDOWN and event.button == 1:
				