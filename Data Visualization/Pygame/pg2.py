import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Smart Rockets')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
car_width = 73

clock = pygame.time.Clock()
car_img = pygame.image.load('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/Pygame/racecar.png')

def objects(x, y, w, h, col):
	pygame.draw.rect(game_display, col, [x, y, w, h])

def car(x, y):
	game_display.blit(car_img, (x, y))

def text_objects(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()

def message_display(text):
	large_text = pygame.font.Font('freesansbold.ttf', 115)
	m_text_surface, m_text_rect = text_objects(text, large_text)
	m_text_rect.center = ((display_width/2), (display_height/2))
	game_display.blit(m_text_surface, m_text_rect)
	pygame.display.update()
	time.sleep(2)

def crash():
	message_display('You Crashed')
	game_loop()

def game_loop():
	# starting points for our car
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	crashed = False
	x_change = 0
	o_x = random.randrange(0, display_width)
	o_y = -600
	o_speed = 7
	o_w = 100
	o_h = 100

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		game_display.fill(white)

		objects(o_x, o_y, o_w, o_h, black)
		o_y += o_speed
		car(x, y)

		if x > display_width - car_width or x < 0:
			crash()

		if o_y > display_height:
			o_y = 0 - o_h
			o_x = random.randrange(0, display_width)

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()