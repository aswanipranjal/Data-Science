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

	def create_world(self):
		self.space = pymunk.Space()
		self.space.gravity = Vec2d(0., -900.)
		self.space.sleep_time_threshold = 0.3

		static_lines = [pymunk.Segment(self.space.static_body, Vec2d(20, 55), Vec2d(600, 55), 1),
						pymunk.Segment(self.space.static_body, Vec2d(550, 55), Vec2d(550, 400), 1)]

		