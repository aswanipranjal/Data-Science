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

# left flipper
l_flipper_body = pymunk.Body(mass, moment)
l_flipper_body.position = 150, 100
l_flipper_shape = pymunk.Poly(l_flipper_body, [(-x, y) for x, y in fp])
space.add(l_flipper_body, l_flipper_shape)

l_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_flipper_joint_body.position = l_flipper_body.position
j = pymunk.PinJoint(l_flipper_body, l_flipper_joint_body, (0, 0), (0, 0))
s = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.15, 20000000, 900000)
space.add(j, s)

r_flipper_shape.group = l_flipper_shape.group = 1
r_flipper_shape.elasticity = l_flipper_shape.elasticity = 0.4

# bumpers
for p in [(240, 500), (360, 500)]:
	body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	body.position = p
	shape = pymunk.Circle(body, 10)
	shape.elasticity = 1.5
	space.add(shape)

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			running = False
		elif event.type == KEYDOWN and event.key == K_p:
			pygame.image.save(screen, 'flipper.png')

		elif event.type == KEYDOWN and event.key == K_j:
			r_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * 40000, (-100, 0))
		elif event.type == KEYDOWN and event.key == K_f:
			l_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * -40000, (-100, 0))
		elif event.type == KEYDOWN and event.key == K_b:
			mass = 1
			radius = 25
			inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
			body = pymunk.Body(mass, inertia)
			x = random.randint(115, 350)
			body.position = x, 400
			shape = pymunk.Circle(body, radius, (0, 0))
			shape.elasticity = 0.95
			space.add(body, shape)
			balls.append(shape)

	screen.fill(THECOLORS['white'])
	space.debug_draw(draw_options)

	r_flipper_body.position = 450, 100
	l_flipper_body.position = 150, 100
	r_flipper_body.velocity = l_flipper_body.velocity = 0, 0
	