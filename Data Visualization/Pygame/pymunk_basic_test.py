import pymunk
import pymunk.util
from pymunk import Vec2d
import sys
import math
import random

def main():
	space = pymunk.Space()
	space.gravity = (0.0, -900.0)

	balls = []

	ticks_to_next_ball = 10
	for x in range(5000) :