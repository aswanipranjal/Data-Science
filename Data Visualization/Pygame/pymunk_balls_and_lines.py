import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d

X, Y = 0, 1
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def flipy(y):
	# converts chipmunk physics to pygame coordinates
	return -y + 600

def mouse_coll_func(arbiter, space, data):
	# simple callback to increase the radius of circles touching the mouse
	s1, s2 = arbiter.shapes
	s2.unsafe_set_radius(s2.radius + 0.15)
	return False

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	running = True

	space = pymunk.Space()
	space.gravity = 0.0, -900.0

	balls = []

	mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
	mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
	mouse_shape.collision_type = COLLTYPE_MOUSE
	space.add(mouse_shape)
	space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL).pre_solve=mouse_coll_func

	# static line
	line_point1 = None
	static_lines = []
	run_physics = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False

			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False

			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'balls_and_lines.png')

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				p = event.pos[X], flipy(event.pos[Y])
				body = pymunk.Body(10, 100)
				body.position = p
				shape = pymunk.Circle(body, 10, (0, 0))
				shape.friction = 0.5
				shape.collision_type = COLLTYPE_BALL
				space.add(body, shape)
				balls.append(shape)

			elif event.type == MOUSEBUTTONDOWN and event.button == 3:
				if line_point1 is None:
					line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))

			elif event.type == MOUSEBUTTONUP and event.button == 3:
				if line_point1 is not None:
					line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
					body = pymunk.Body(body_type=pymunk.Body.STATIC)
					shape = pymunk.Segment(body, line_point1, line_point2, 0.0)
					shape.friction = 0.99
					space.add(shape)
					static_lines.append(shape)
					line_point1 = None

			elif event.type == KEYDOWN and event.key == K_SPACE:
				run_physics = not run_physics

		p = pygame.mouse.get_pos()
		mouse_pos = Vec2d(p[X], flipy(p[Y]))
		mouse_body.position = mouse_pos

		if pygame.key.get_mods() & KMOD_SHIFT and pygame.mouse.get_pressed()[0]:
			body = pymunk.Body(10, 10)
			body.position = mouse_pos
			shape = pymunk.Circle(body, 10, (0, 0))
			shape.collision_type = COLLTYPE_BALL
			space.add(body, shape)
			balls.append(shape)

		if run_physics:
			dt = 1.0/60.0
			for x in range(1):
				space.step(dt)

		screen.fill(THECOLORS['white'])

		font = pygame.font.Font(None, 16)
		text = '''LMB: Create ball
				  LMB + Shift: Create many balls
				  RMB: Drag to create wall
				  Space: Pause physics simulation'''
		y = 5
		for line in text.splitlines():
			text = font.render(line, 1, THECOLORS['black'])
			screen.blit(text, (5, y))
			y += 10

		for ball in balls:
			r = ball.radius
			v = ball.body.position
			rot = ball.body.rotation_vector
			p = int(v.x), int(flipy(v.y))
			p2 = Vec2d(rot.x, -rot.y) * r * 0.9
			pygame.draw.circle(screen, THECOLORS['blue'], p, int(r), 2)
			pygame.draw.line(screen, THECOLORS['red'], p, p + 2)

		if line_point1 is not None:
			p1 = line_point1.x, flipy(line_point1.y)
			p2 = mouse_pos.x, flipy(mouse_pos.y)
			pygame.draw.lines(screen, THECOLORS['black'], False, [p1, p2])
			