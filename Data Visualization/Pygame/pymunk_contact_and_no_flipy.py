import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

def draw_collision(arbiter, space, data):
	for c in arbiter.contact_point_set.points:
		r = max(3, abs(c.distance * 5))
		r = int(r)
		p = tuple(map(int, c.point_a))
		pygame.draw.circle(data['surface'], THECOLORS['red'], p, r, 0)

def main():
	global contact
	global shape_to_remove

	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True
	