import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,  255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((800,600))
game_display.fill(black)

# converting the game_displayinto a pixel array
pix_ar = pygame.PixelArray(game_display)
pix_ar[10][20] = green

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()