import sys

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

def create_arrow():
	vs = [(-30, 0), (0, 3), (10, 0), (0, -3)]
	mass = 1
	moment = pymunk.moment_for_poly(mass, vs)
	arrow_body = pymunk.Body(mass, moment)

	arrow_shape = pymunk.Poly(arrow_body, vs)
	arrow_shape.friction = .5
	arrow_shape.collision_type = 1

def stick_arrow_to_target(space, arrow_body, target_body, position, flying_arrows):
	pivot_joint = pymunk.PivotJoint(arrow_body, target_body, position)
	phase = target_body.angle - arrow_body.angle
	gear_joint = pymunk.GearJoint(arrow_body, target_body, phase, 1)
	space.add(pivot_joint)
	space.add(gear_joint)
	try:
		flying_arrows.remove(arrow_body)
	except:
		pass

def post_solve_arrow_hit(arbiter, space, data):
	if arbiter.total_impulse.length > 300:
		a, b = arbiter.shapes
		position = arbiter.contact_point_set.points[0].point_a
		b.collision_type = 0
		b.group = 1
		other_body = a.body
		arrow_body = b.body
		space.add_post_step_callback(stick_arrow_to_target, arrow_body, other_body, position, data["flying_arrows"])

width, height = 690, 600
def main():
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()
	running = True
	font = pygame.font.Sysfont('Arial', 16)

	# physics
	space = pymunk.Space()
	space.gravity = 0, -1000
	draw_options = pymunk.pygame_util.DrawOptions(screen)

	# walls
	static = [pymunk.Segment(space.static_body, (50, 50), (50, 550), 5),
			  pymunk.Segment(space.static_body, (50, 550), (650, 660), 5),
			  pymunk.Segment(space.static_body, (650, 550), (650, 50), 5),
			  pymunk.Segment(space.static_body, (50, 50), (650, 50), 5)]

	b2 = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	static.append(pymunk.Circle(b2, 30))
	b2.position = 300, 400

	for s in static:
		s.friction = 1.
		s.group = 1
	space.add(static)

	# cannon
	cannon_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	cannon_shape = pymunk.Circle(cannon_body, 25)
	cannon_shape.sensor = True
	cannon_shape.color = (255, 50, 50)
	cannon_body.position = 100, 100
	space.add(cannon_shape)

	arrow_body, arrow_shape = create_arrow()
	space.add(arrow_shape)

	flying_arrows = []
	handler = space.add_collision_handler(0, 1)
	handler.data["flying_arrows"] = flying_arrows
	handler.post_solve = post_solve_arrow_hit

	while running:
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and (event.key in [K_ESCAPE, K_q]):
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				start_time = pygame.time.get_ticks()
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, "arrows.png")
			elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				end_time = pygame.time.get_ticks()

				diff = end_time - start_time
				power = max(min(diff, 1000), 10) * 1.5
				impulse = power * Vec2d(1, 0)
				impulse.rotate(arrow_body.angle)
				arrow_body.apply_impulse_at_world_point(impulse, arrow_body.position)
				space.add(arrow_body)
				flying_arrows.append(arrow_body)
				arrow_body, arrow_shape = create_arrow()
				space.add(arrow_shape)

		keys = pygame.key.get_pressed()

		speed = 2.5
		if (keys[K_UP]):
			cannon_body.position += Vec2d(0, 1) * speed
		if (keys[K_DOWN]):
			cannon_body.position += Vec2d(0, -1) * speed
		if (keys[K_LEFT]):
			cannon_body.position += Vec2d(-1, 0) * speed
		if (keys[K_RIGHT]):
			cannon_body.position += Vec2d(1, 0) * speed