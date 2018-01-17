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
