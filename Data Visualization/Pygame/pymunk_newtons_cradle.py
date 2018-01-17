import os
import sys
import random

description = """
---- Newton's Cradle ----
A screensaver version of Newton's Cradle with an interactive mode
/s run in fullscreen screensaver mode
/p display a preview of the screensaver using a window handler
/i interactive mode
"""

if len(sys.argv) < 2:
	print(description)
	sys.exit()

is_interactive = False
display_flags = 0
if sys.argv[1] == "/p": # preview mode
	os.environ['SDL_VIDEODRIVER'] = 'windib'
	os.environ['SDL_WINDOWID'] = sys.argv[2]
	display_size = (100, 100)
	is_interactive = False

import pygame
from pygame.locals import *
from pygame.color import *

if sys.argv[1] == "/s": # fullscreen screensaver mode
	display_size = (0, 0)
	is_interactive = False
	display_flags = display_flags | FULLSCREEN # FULLSCREEN | DOUBLEBUF | HWSURFACE
elif sys.argv[1] == "/i": # interactive
	display_size = (600, 600)
	is_interactive = True

import pymunk as pm
from pymunk import Vec2d

def drawcircle(image, color, origin, radius, width=0):
	if width == 0:
		pygame.draw.circle(image, color, origin, int(radius))
	else:
		if radius > 65534/5:
			radius = 65534/5
		circle = pygame.Surface([radius*2 + width, radius*2 + width]).convert_alpha()
		circle.fill([0, 0, 0])
		pygame.draw.circle(circle, color, [circle.get_width()/2, circle.get_height()/2], radius+(width/2))
		if int(radius - (width/2)) > 0:
			pygame.draw.circle(circle, [0, 0, 0, 0], [circle.get_width()/2, circle.get_height()/2], abs(int(radius-(width/2))))
		image.blit(circle, [origin[0] - (circle.get_width()/2), origin[1] - (circle.get_height()/2)])

def reset_bodies(space):
	for body in space.bodies:
		body.position = Vec2d(body.start_position)
		body.force = 0, 0
		body.torque = 0
		body.velocity = 0, 0
		body.angular_velocity = 0
	color = random.choice(list(THECOLORS.values()))
	for shape in space.shapes:
		shape.color = color

def main():
	pygame.init()
	screen = pygame.display.set_mode(display_size, display_flags)
	width, height= screen.get_size()

	def to_pygame(p):
		'''A hacky way to convert pymunk to pygame coordinates'''
		return int(p.x), int(-p.y + height)

	def from_pygame(p):
		return to_pygame(p)

	clock = pygame.time.Clock()
	running = True
	font = pygame.font.Font(None, 16)

	# physics
	space = pm.Space()
	space.gravity = (0.0, -1900.0)
	space.damping = 0.999 # to prevent it from blowing up
	mouse_body = pm.Body(body_type=pm.Body.KINEMATIC)

	bodies = []
	for x in range(-100, 150, 50):
		x += width / 2
		offset_y = height / 2
		mass = 10
		radius = 25
		moment = pm.moment_for_circle(mass, 0, radius, (0, 0))
		body = pm.Body(mass, moment)
		body.position = (x, -125 + offset_y)
		body.start_position = Vec2d(body.position)
		shape = pm.Circle(body, radius)
		shape.elasticity = 0.9999999
		bodies.append(body)
		pj = pm.PinJoint(space.static_body, body, (x, 125 + offset_y), (0, 0))
		space.add(pj)

	reset_bodies(space)
	selected = None

	if not is_interactive:
		pygame.time.set_timer(USEREVENT+1, 70000) # apply force
		pygame.time.set_timer(USEREVENT+2, 120000) # reset
		pygame.event.post(pygame.event.Event(USEREVENT+1))
		pygame.mouse.set_visible(False)

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'newtons_cradle.png')
			if event.type == pygame.USEREVENT+1:
				r = random.randint(1, 4)
				for body in bodies[0:r]:
					body.apply_impulse_at_local_point((-6000, 0))
			