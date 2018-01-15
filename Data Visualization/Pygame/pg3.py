import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,  255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((800,600))
game_display.fill(black)

# converting the game_display into a pixel array
pix_ar = pygame.PixelArray(game_display)
pix_ar[10][20] = green

pygame.draw.line(game_display, blue, (100,  200), (300, 450), 5)
pygame.draw.rect(game_display, red, (400, 400, 50, 25))
pygame.draw.circle(game_display, white, (150, 150), 75)
pygame.draw.polygon(game_display, green, ((25, 75), (76, 125), (250, 375), (400, 25), (60, 540)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()