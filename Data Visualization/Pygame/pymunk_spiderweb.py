__docformat__ = "reStructuredText"

import math
import random
import pyglet

import pymunk
from pymunk.vec2d import Vec2d

config = pyglet.gl.Config(sample_buffers=1, samples=2, double_buffer=True)
window = pyglet.window.Window(config=config, vsync=False)
space = pymunk.Space()

space.gravity = 0, -900
space.damping = .999
c = Vec2d(window.width / 2., window.height / 2.)

# web
web_group = 1
bs = []
dist = .3

cb = pymunk.Body(1, 1)
cb.position = c
s = pymunk.Circle(cb, 15)
s.filter = pymunk.ShapeFilter(group=web_group)
s.ignore_draw = True
space.add(cb, s)