import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_width = 73

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Smart Rockets')
clock = pygame.time.Clock()
car_img = pygame.image.load('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/Pygame/racecar.png')

def objects_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render('Dodged: ' + str(count), True, black)
	game_display.blit(text, (0, 0))

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

def quit_game():
	pygame.quit()
	quit()

def button(msg, x, y, w, h, i_color, a_color, action=None):
	'''
	msg: message to be displayed
	x: starting x-coordinate
	y: starting y-coordinate
	w: width
	h: height
	i_color: inactive color
	a_color: active color
	'''
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	print(click)

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(game_display, a_color, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(game_display, i_color, (x, y, w, h))

	small_text = pygame.font.Font('freesansbold.ttf', 20)
	m_text_surface, m_text_rect = text_objects(msg, small_text)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2)))
	game_display.blit(m_text_surface, m_text_rect)

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		game_display.fill(white)
		large_text = pygame.font.Font('freesansbold.ttf', 115)
		m_text_surface, m_text_rect = text_objects('Smart Rockets', large_text)
		m_text_rect.center = ((display_width/2), (display_height/2))
		game_display.blit(m_text_surface, m_text_rect)

		button('GO!', 100, 450, 100, 50, green, bright_green, game_loop)
		button('Exit', 550, 450, 100, 50, red, bright_red, quit_game)

		pygame.display.update()
		clock.tick(15)

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
	o_count = 0
	dodged = 0

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
		objects_dodged(dodged)

		if x > display_width - car_width or x < 0:
			crash()

		if o_y > display_height:
			o_y = 0 - o_h
			o_x = random.randrange(0, display_width)
			dodged += 1
			o_speed += 1
			o_w += (dodged * 1.2)

		if y < o_y + o_h:
			# print('y crossover')

			if x > o_x and x < o_x + o_w or x + car_width > o_x and x + car_width < o_x + o_w:
				# print('x crossover')
				crash()

		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()