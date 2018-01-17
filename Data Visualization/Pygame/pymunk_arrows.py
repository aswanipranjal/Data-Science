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
			  