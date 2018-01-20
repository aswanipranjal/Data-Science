import os
import sys
import math
import random

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

width, height = 600, 600

collision_types = {
	'ball': 1,
	'brick': 2,
	'bottom': 3,
	'player': 4,
}