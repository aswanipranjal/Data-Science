import pygame

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Smart Rockets')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
car_img = pygame.image.load('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/Pygame/racecar.png')

def car(x, y):
	game_display.blit(car_img, (x, y))

# starting points for our car
x = (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	game_display.fill(white)
	car(x, y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()