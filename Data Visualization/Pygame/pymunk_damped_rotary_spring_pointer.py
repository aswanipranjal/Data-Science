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
