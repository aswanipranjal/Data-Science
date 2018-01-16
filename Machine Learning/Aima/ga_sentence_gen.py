import pygame
import time
import random
import search

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Phrase Generator')
clock = pygame.time.Clock()

target = 'To be or not to be.'
max_population = 500
mutation_rate = 0.01
# possible genes
u_case = [chr(x) for x in range(65, 91)]
l_case = [chr(x) for x in range(97, 123)]
u_case.extend(l_case)

def loop():
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		pygame.display.update()
		clock.tick(60)

print(u_case)
loop()
pygame.quit()
quit()