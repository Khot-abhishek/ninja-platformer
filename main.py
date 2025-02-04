import sys
import pygame


class Game:
	def __init__(self):
		pygame.init()

		SCREEN_RESOLUTION = (640,480)
		pygame.display.set_caption('Ninja Game')
		self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)

		self.clock = pygame.time.Clock()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print('over')
					pygame.quit()
					sys.exit()

			pygame.display.update()
			self.clock.tick(60)		

Game().run()


