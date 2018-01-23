import pygame
from pygame.locals import *

def name():
	pygame.init()
	screen = pygame.display.set_mode((480, 360))
	name = ''
	font = pygame.font.Font(None, 50)
	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.unicode.isalpha():
					name += event.unicode
				elif event.key == K_BACKSPACE:
					name = name[:-1]
				elif event.key == K_RETURN:
					name = ''
			elif event.type == QUIT:
				return