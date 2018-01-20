import sys
import random
import pygame
from pygame.locals import *

import pymunk
import pymunk.pygame_util

def add_ball(space):
	mass = 1
	radius = 14
	inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
	body = pymunk.Body(mass, inertia)
	x = random.randint(120, 380)
	body.position = x, 550
	shape = pymunk.Circle(body, radius, (0, 0))
	space.add(body, shape)
	return shape

def add_L(space):
	rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
	rotation_center_body.position = (300, 300)

	rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
	rotation_limit_body.position = (200, 300)

	body = pymunk.Body(10, 10000)
	body.position = (300, 300)
	l1 = pymunk.Segment(body, (-150.0, 0), (255.0, 0.0), 1)
	l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 1)

	rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
	joint_limit = 25
	rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100, 0), (0, 0), 0, joint_limit)

	space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
	return l1, l2