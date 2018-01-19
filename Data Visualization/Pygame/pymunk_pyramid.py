import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

class Pyramid:
	def __init__(self):
		self.running = True
		self.drawing = True
		self.w, self.h = 600, 600
		self.screen = pygame.display.set_mode((self.w, self.h))
		self.clock = pygame.time.Clock()

		self.space = pymunk.Space()
		self.space.gravity = (0.0, -900.0)
		self.space.sleep_time_threshold = 0.3

		