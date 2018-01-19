import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

def draw_collision(arbiter, space, data):
	for c in arbiter.contact_point_set.points:
		r = max(3, abs(c.distance * 5))
		r = int(r)
		p = tuple(map(int, c.point_a))
		pygame.draw.circle(data['surface'], THECOLORS['red'], p, r, 0)

def main():
	global contact
	global shape_to_remove

	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True

	# physics
	space = pm.Space()
	space.gravity = (0.0, 900.0)

	balls = []

	static_body = pm.Body(body_type = pm.Body.STATIC)
	static_lines = [pm.Segment(static_body, (111.0, 320.0), (407.0, 354.0), 0.0),
					pm.Segment(static_body, (407.0, 354.0), (407.0, 257.0), 0.0)]
	space.add(static_lines)

	ticks_to_next_ball = 10
	ch = space.add_collision_handler(0, 0)	
	ch.data['surface'] = screen
	ch.post_solve = draw_collision

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False			