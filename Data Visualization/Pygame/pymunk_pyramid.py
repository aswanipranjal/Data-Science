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

		shape = pymunk.Segment(self.space.static_body, (5, 100), (595, 100), 1.0)
		shape.friction = 1.0
		self.space.add(shape)

		x = Vec2d(-270, 7.5) + (300, 100)
		y = Vec2d(0, 0)
		deltaX = Vec2d(0.5625, 1.1) * 20
		deltaY = Vec2d(1.125, 0.0) * 20

		for i in range(25):
			y = Vec2d(x)
			for j in range(i, 25):
				size = 10
				points = [(-size, -size), (-size, size), (size, size), (size, -size)]
				mass = 1.0
				moment = pymunk.moment_for_poly(mass, points, (0, 0))
				body = pymunk.Body(mass, moment)
				body.position = y
				shape = pymunk.Poly(body, points)
				shape.friction = 1
				self.space.add(body, shape)

				y += deltaY
			x += deltaX
		self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

	def run(self):
		while self.running:
			self.loop()

	def loop(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				self.running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(self.screen, 'box2d_pyramid.png')
			elif event.type == KEYDOWN and event.key == K_d:
				self.drawing = not self.drawing

		fps = 30.
		dt = 1.0 / fps / 5
		self.space.step(dt)
		if self.drawing:
			self.draw()

		self.clock.tick(fps)
		pygame.display.set_caption(f'fps: {str(self.clock.get_fps())}')

	def draw(self):
		self.screen.fill(THECOLORS['white'])
		self.space.debug_draw(self.draw_options)
		pygame.display.flip()

def main():
	pyramid = Pyramid()
	pyramid.run()

if __name__ == '__main__':
	main()