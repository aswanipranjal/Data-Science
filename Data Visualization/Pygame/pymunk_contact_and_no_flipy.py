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
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'contact_and_no_flipy.png')

		ticks_to_next_ball -= 1
		if ticks_to_next_ball <= 0:
			ticks_to_next_ball = 100
			mass = 10
			radius = 25
			inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
			body = pm.Body(mass, inertia)
			x = random.randint(115, 350)
			body.position = x, 200
			shape = pm.Circle(body, radius, (0, 0))
			space.add(body, shape)
			balls.append(shape)

		screen.fill(THECOLORS['white'])

		# draw stuff
		balls_to_remove = []
		for ball in balls:
			if ball.body.position.y > 400: balls_to_remove.append(ball)
			p = tuple(map(int, ball.body.position))
			pygame.draw.circle(screen, THECOLORS['blue'], p, int(ball.radius), 2)

		for ball in balls_to_remove:
			space.remove(ball, ball.body)
			balls.remove(ball)

		for line in static_lines:
			body = line.body
			p1 = body.position + line.a.rotated(body.angle)
			p2 = body.position + line.b.rotated(body.angle)
			pygame.draw.lines(screen, THECOLORS['lightgray'], False, [p1, p2])

		