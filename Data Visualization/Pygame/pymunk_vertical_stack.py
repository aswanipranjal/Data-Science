import math

import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse

import pymunk
from pymunk import Vec2d
import pymunk.pyglet_util

class Main(pyglet.window.Window):
	def __init__(self):
		pyglet.window.Window.__init__(self, vsync=False)
		self.set_caption('Vertical Stack from Box2D')

		pyglet.clock.schedule_interval(self.update, 1/60.0)
		self.fps_display = pyglet.clock.ClockDisplay()
		self.text = pyglet.text.Label('Press space to fire bullet', font_size=10, x=10, y=400)
		self.create_world()
		self.draw_options = pymunk.pyglet_util.DrawOptions()
		self.draw_options.flags = self.draw_options.DRAW_SHAPES