__docformat__ = 'reStructuredText'

import sys

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d, BB
import pymunk.pygame_util
import pymunk.autogeometry

def draw_helptext(screen):
	font = pygame.font.Font(None, 16)
	text = ['LMB (hold): Draw pink color',
			'Shift + LMB (hold): Create balls',
			'g: Generate segments from pink color drawing',
			'r: Reset',]
	y = 5
	for line in text:
		text = font.render(line, 1, THECOLORS['black'])
		screen.blit(text, (5, y))
		y += 10

def generate_geometry(surface, space):
	for s in space.shapes:
		if hasattr(s, 'generated') and s.generated:
			space.remove(s)

	def sample_func(point):
		try:
			p = int(point.x), int(point.y)
			color = surface.get_at(p)
			return color.hsla[2] # use lightness
		except:
			return 0

	line_set = pymunk.autogeometry.PolylineSet()
	def segment_func(v0, v1):
		line_set.collect_segment(v0, v1)

	pymunk.autogeometry.march_soft(BB(0, 0, 599, 599), 60, 60, 90, segment_func, sample_func)

	for polyline in line_set:
		line = pymunk.autogeometry.simplify_curves(polyline, 1.)

		for i in range(len(line) - 1):
			p1 = line[i]
			p2 = line[i+1]
			shape = pymunk.Segment(space.static_body, p1, p2, 1)
			shape.friction = .5
			shape.color = pygame.color.THECOLORS['red']
			shape.generated = True
			space.add(shape)