import pygame

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

def car(x, y):
	game_display.blit(car_img, (x, y))

def game_loop():
	# starting points for our car
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	crashed = False
	x_change = 0

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True

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
		car(x, y)

		if x > display_width - car_width or x < 0:
			crashed = True

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()