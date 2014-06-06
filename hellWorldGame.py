import pygame,sys
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello , Welcome to Snake world')


# set up the colors

BLACK = (  0,   0,   0)

WHITE = (255, 255, 255)

RED = (255,   0,   0)

GREEN = (  0, 255,   0)

BLUE = (  0,   0, 255)

# drawing 2 lines

pygame.draw.line(DISPLAYSURF, BLUE, (160,20), (240, 20))


pygame.draw.line(DISPLAYSURF, BLUE, (160,40), (240, 40))



while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()