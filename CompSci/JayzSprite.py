import pygame, math, sys, os
from pygame.locals import *

screen = pygame.display.set_mode((1000, 500))
clock =  pygame.time.Clock()

class JayZSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 300
		self.src_image =  pygame.image.load('jayzsprite.png')
		self.src_image = pygame.transform.scale(self.src_image, (125,200))
		self.speed = self.direction = 0

	def update(self):
		if self.position[0] >=0:
			self.position = (self.position[0] - 5, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1050,300)

rect = screen.get_rect()
JayZ = JayZSprite()
JayZ_group = pygame.sprite.Group(JayZ)

while 1:
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_ESCAPE:
			sys.exit(0)
	#RENDERING

	screen.fill((255,255,255))
	JayZ_group.update()
	JayZ_group.draw(screen)
	pygame.display.flip()