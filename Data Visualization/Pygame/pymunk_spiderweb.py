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

for x in range(0, 101):
	b = pymunk.Body(1, 1)
	v = Vec2d.unit()
	v.angle_degrees = x * 18
	scale = window.height / 2. / 6. * .5

	dist += 1 / 18.
	dist = dist ** 1.005

	offset = 0
	offset = [0.0, -0.80, -1.0, -0.80][((x*18) % 360) // 18 % 4]
	offset = .8 + offset
	offset *= dist ** 2.8 / 100.

	v.length = scale * (dist + offset)

	b.position = c + v
	s = pymunk.Circle(b, 15)
	s.filter = pymunk.ShapeFilter(group=web_group)
	s.ignore_draw = True
	space.add(b, s)
	bs.append(b)

def add_joint(a, b):
	rl = a.position.get_distance(b.position) * 0.9
	stiffness = 5000.
	damping = 100
	j = pymunk.DampedSpring(a, b, (0, 0), (0, 0), rl, stiffness, damping)
	j.max_bias = 1000
	space.add(j)

for b in bs[:20]:
	add_joint(cb, b)

for i in range(len(bs)-1):
	add_joint(bs[i], bs[i+1])
	i2 = i + 20
	if len(bs) > i2:
		add_joint(bs[i], bs[i2])

