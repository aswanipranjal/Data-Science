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
