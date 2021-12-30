import pygame, math, sys, os
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((1000, 500))
clock =  pygame.time.Clock()

class KraftSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 200
		self.src_image =  pygame.image.load('KraftPunk.png')
		self.src_image = pygame.transform.scale(self.src_image, (175,100))
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - 10, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1200,200)

rect = screen.get_rect()
kraft = KraftSprite()
kraft_group = pygame.sprite.Group(kraft)

while 1:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_ESCAPE:
			sys.exit(0)
	#RENDERING

	screen.fill((255,255,255))
	kraft_group.update(deltat)
	kraft_group.draw(screen)
	pygame.display.flip()