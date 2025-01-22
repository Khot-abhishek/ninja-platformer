import sys
import pygame

pygame.init()

SCREEN_RESOLUTION = (640,480)

screen = pygame.display.set_mode(SCREEN_RESOLUTION)

clock = pygame.time.Clock()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('over')
			pygame.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(60)