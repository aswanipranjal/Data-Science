__docformat__ = "reStructuredText"

import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True

	space = pymunk.Space()
	draw_options = pymunk.pygame_util.DrawOptions(screen)

	pointer_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

	polygon_shape = [(80, 0), (0, 20), (0, -20)]
	moment = pymunk.moment_for_poly(1, polygon_shape)
	gun_body = pymunk.Body(1, moment)
	gun_body.position = 300, 300
	gun_shape = pymunk.Poyl(gun_body, polygon_shape)

	rest_angle = 0
	stiffness = 125000.
	damping = 6000.

	rotary_spring = pymunk.constraint.DampedRotarySpring(pointer_body, gun_body, rest_angle)
	space.add(gun_body, gun_shape, rotary_spring)

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'damped_rotary_spring_pointer.png')
			elif event.type == pygame.MOUSEMOTION:
				mouse_pos = pymunk.pygame_util.get_mouse_pos(screen)
				pointer_body.position = mouse_pos
				pointer_body.angle = (pointer_body.position - gun_body.position).angle

			elif event.type == KEYDOWN and event.key == K_q:
				rotary_spring.stiffness *= .5
				print(rotary_spring.stiffness, rotary_spring.damping)
			elif event.type == KEYDOWN and event.key == K_w:
				rotary_spring.stiffness *= 2
				print(rotary_spring.stiffness, rotary_spring.damping)
			elif event.type == KEYDOWN and event.key == K_a:
				rotary_spring.damping *= .5
				print(rotary_spring.stiffness, rotary_spring.damping)
			elif event.type == KEYDOWN and event.key == K_s:
				rotary_spring.damping *= 2
