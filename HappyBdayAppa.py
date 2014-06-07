import pygame
from pygame.locals import *

def main():
	#Initialize screen
	pygame.init()
	screen = pygame.display.set_mode(150,150)

	# set up the colors
	BLACK = (  0,   0,   0)
	WHITE = (255, 255, 255)
	RED = (255,   0,   0)
	GREEN = (  0, 255,   0)
	BLUE = (  0,   0, 255)

	# drawing 2 lines

	pygame.draw.line(DISPLAYSURF, BLUE, (160,20), (240, 20))
	pygame.draw.line(DISPLAYSURF, BLUE, (160,40), (240, 40))

	# Displaying text
	font = pygame.font.Font(None,36)
	text = font.render("Hello There",1,(10,10,10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text,textpos)

	# blit everything to the screen 
	screen.blit(background,(0,0))
	pygame.display.flip()
	

	while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
