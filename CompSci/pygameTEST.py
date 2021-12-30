#INIT
import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

class CarSprite(pygame.sprite.Sprite):
	MAX_FORWARD_SPEED = 10
	MAX_REVERSE_SPEED = 10
	ACCELERATION = 2
	TURN_SPEED = 5

	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.src_image = pygame.image.load(image)
		self.speed = self.direction = 0
		self.k_left = self.k_right = self.k_up = self.k_down = 0

	def update(self, deltat):
		#SIMULATION
		# self.speed += (self.k_up + self.k_down)
		# if self.speed > self.MAX_FORWARD_SPEED: 
		# 	self.speed = self.MAX_FORWARD_SPEED
		# if self.speed < -self.MAX_REVERSE_SPEED:
		# 	self.speed = -self.MAX_REVERSE_SPEED
		# self.direction += (self.k_right + self.k_left)
		#x, y = self.position
		# rad = self.direction * math.pi / 180
		# x += -self.speed * math.sin(rad)
		# y += -self.speed * math.cos(rad)
		#self.position = (x, y)
		self.image = pygame.transform.rotate(
			self.src_image, self.direction)
		self.rect = self.image.get_rect()
		#self.rect.center = self.position

#Create a car and run
rect = screen.get_rect()
car = CarSprite('HannableCop.png', rect.center)
#create a sprite group that contains just that image
car_group = pygame.sprite.RenderPlain(car)

while 1:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		# down = event.type == KEYDOWN
		# if event.key == K_RIGHT: 
		# 	car.k_right = down * -5
		# elif event.key == K_LEFT:
		# 	car.k_left = down * 5
		# elif event.key == K_UP:
		# 	car.k_up = down * 2
		# elif event.key == K_DOWN:
		# 	car.k_down = down * -2
		elif event.key == K_ESCAPE:
			sys.exit(0)

	#RENDERING
	screen.fill((255,255,255))
	car_group.update(deltat)
	car_group.draw(screen)
	pygame.display.flip()


