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