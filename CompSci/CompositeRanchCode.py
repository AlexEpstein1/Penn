import pygame, math, sys
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

def end_game():
	#Needs to be better :-)
	print("End of Game")


class BackgroundSprite(pygame.sprite.Sprite):
	def __init__(self, position, flip_image=False):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.src_image =  pygame.image.load('../Sprites/RanchBackground.png')
		self.src_image = pygame.transform.scale(self.src_image, (1600,500))
		if flip_image: self.src_image = pygame.transform.flip(self.src_image, True, False)
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0]>= -1100:
			self.position = (self.position[0] - 5, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1600,250)

# class Score(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.font = pygame.font.SysFont('Arial', 15)
#         pygame.display.set_caption('Box Test')
#         self.screen = pygame.display.set_mode((600,400), 0, 32)
#         self.screen.fill((255,255,255))
#         pygame.display.update()

#     def addRect(self):
#         self.rect = pygame.draw.rect(self.screen, (0,0,0), (445, 0, 598, 45), 2)
#         pygame.display.update()

#     def update_text(self):
#         self.screen.blit(self.font.render('Ranch Collected: ' + str(eric.ranch_collected), True, (255,0,0)), (450, 22))
#         pygame.display.update()


class EricSprite(pygame.sprite.Sprite):
	MOVEMENT_SPEED = 5

	START_HEIGHT = 340
	APEX_HEIGHT = 150

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pos_x = 10
		self.pos_y = self.START_HEIGHT
		self.position = self.pos_x, self.pos_y
		self.src_image = pygame.image.load("../Sprites/EricHorse–Standing.png")
		self.src_image = pygame.transform.scale(self.src_image, (100, 105))
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (100, 50))
		self.rect.topleft = self.position
		self.speed = self.MOVEMENT_SPEED
		self.walking_images = ["../Sprites/EricHorse–Standing.png", "../Sprites/EricHorse-walking1.png", "../Sprites/EricHorse-walking2.png"]

		self.ranch_collected = 0
		self.distance = 0

		
		self.standing = True
		self.ducking = False
		self.jumping = False
		self.jump_acel = 2

		# print(self.ranch_collected)

	def move_left(self):
		self.pos_x -= self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

	def move_right(self):
		self.pos_x += self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

	def jump(self):
		self.jumping = True
		self.standing = False
		self.ducking = False

	def duck(self):
		self.jumping = False
		self.standing = False
		self.ducking = True

	def add_ranch(self):
		self.ranch_collected += 1
		print(self.ranch_collected)

	def update(self):
		self.distance += 1
		'''Sprite Boundaries'''
		if self.pos_x <= 0:
			self.pos_x = 0
		elif self.pos_x >= 915:
			self.pos_x = 915 
		'''Deals with jumps'''
		if self.standing:
			self.JUMP_VELOCITY = -25
			self.src_image = pygame.image.load(self.walking_images[(self.distance % 3) - 1])
			self.src_image = pygame.transform.scale(self.src_image, (100, 105))
			if self.pos_y >= self.START_HEIGHT:
				self.pos_y = self.START_HEIGHT
		elif self.jumping:
			self.src_image = pygame.image.load("../Sprites/EricHorse-jumping.png")
			self.src_image = pygame.transform.scale(self.src_image, (100, 105))
			self.JUMP_VELOCITY += self.jump_acel
			self.pos_y += self.JUMP_VELOCITY
			if self.pos_y >= self.START_HEIGHT:
				self.standing = True
				self.jumping = False
				self.ducking = False
				self.pos_y = self.START_HEIGHT
		elif self.ducking:
			key = pygame.key.get_pressed()
			if not(key[pygame.K_DOWN]):
				self.standing = True
				self.jumping = False
				self.ducking = False
				self.pos_y = self.START_HEIGHT
			self.src_image = pygame.image.load("../Sprites/EricHorse–Ducking.png")
			self.src_image = pygame.transform.scale(self.src_image, (90, 80))
			self.pos_y = self.START_HEIGHT + 30
		self.position = self.pos_x, self.pos_y
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (100, 50))
		self.rect.topleft = self.position


class CopSprite(pygame.sprite.Sprite):
	MAX_SPEED =  10
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 320
		self.src_image =  pygame.image.load("../Sprites/HannableCop.png")
		self.src_image = pygame.transform.scale(self.src_image, (75,105))
		self.speed = self.direction = 0
		# self.rect = self.src_image.get_rect()
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (25, 100))
		self.rect.topleft = self.position
		

	def update(self, deltat):
		# print(self.src_image.get_size())
		
		# if self.position[0] >=0:
		self.position = (self.position[0] - 10, self.position[1])
		self.image = pygame.transform.rotate(self.src_image, self.direction)
			# self.rect = self.src_image.get_rect()
			# self.rect = pygame.rect.Rect((self.position[0] + 500, self.position[1]), (25, 100))
			# self.rect.topleft = self.position
			# pygame.draw.rect(self.rect, "")
		if self.position[0] <= 0:
			self.position = (1000, 320)
			while abs(self.position[0] - kraft_punk.position[0]) < 350:
				self.position = (randint(1000, 2000),320)
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (25, 100))
		self.rect.topleft = self.position

class KraftSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 292
		while abs(self.position[0] - cop.position[0]) < 350:
			self.position = (randint(1200, 2000), 292)
		self.src_image =  pygame.image.load('../Sprites/KraftPunk.png')
		self.src_image = pygame.transform.scale(self.src_image, (175,100))
		self.speed = self.direction = 0
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (150, 50))
		self.rect.topleft = self.position

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - 10, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			
		else:
			self.position = (1200,292)
			while abs(self.position[0] - cop.position[0]) < 350:
				self.position = (randint(1200, 2000), 292)
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (150, 50))
		self.rect.topleft = self.position

class RanchSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = (randint(1200, 1500),300)
		while abs(self.position[0] - cop.position[0]) < 150:
			self.position = (randint(1200, 1500),300)
		self.ranch_images = ['../Sprites/Ranch.png', '../Sprites/SirachaRanch.png']
		self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
		self.src_image = pygame.transform.scale(self.src_image, (45,75))
		self.speed = self.direction = 0

		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), self.src_image.get_size())
		self.rect.topleft = self.position

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - 10, self.position[1] - randint(-3,3))
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			
		else:
			self.position = (randint(1200, 1500),300)
			while abs(self.position[0] - cop.position[0]) < 150:
				self.position = (randint(1200, 1500),300)
			self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
			self.src_image = pygame.transform.scale(self.src_image, (45,75))
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), self.src_image.get_size())
		self.rect.topleft = self.position

pygame.display.set_caption('Ranch It up')

cop = CopSprite()
cop_group = pygame.sprite.Group(cop)

kraft_punk = KraftSprite()
kraft_group = pygame.sprite.Group(kraft_punk)

ranch = RanchSprite()
ranch_group = pygame.sprite.Group(ranch)

background1 = BackgroundSprite((800,250))
background2 = BackgroundSprite((2100,250), True)
background_group = pygame.sprite.Group(background1)
background_group.add(background2)

eric = EricSprite()
screen.fill((255, 255, 255))
screen.blit(eric.src_image, eric.position)
pygame.display.flip()

pygame.init()
score_font = pygame.font.SysFont("comicsansms", 15)
score = score_font.render("Ranch Collected: " + str(eric.ranch_collected), True, (255, 0, 0))

pygame.mixer.init()
pygame.mixer.music.load("../Audio/RanchItUp.wav")
pygame.mixer.music.play(1)

ranch_sounds_src = ["../Audio/SupMelo.wav", "../Audio/BuzzMeMullato.wav", "../Audio/RANCH.wav"]

while 1:
	print(cop.position[0], kraft_punk.position[0])
	'''Eric Andre Movement'''
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_DOWN:
			eric.duck()
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		eric.move_left()
	if key[pygame.K_RIGHT]:
		eric.move_right()
	if key[pygame.K_SPACE] or key[pygame.K_UP]:
		if eric.standing:
			eric.jump()
	if key[pygame.K_DOWN]:
		eric.duck()
	if key[pygame.K_ESCAPE]:
		sys.exit()

	'''Collision Detection'''
	if pygame.sprite.spritecollide(eric, cop_group, True) or pygame.sprite.spritecollide(eric, kraft_group, True):
		end_game()
		pygame.time.delay(1000)
		sys.exit()
	if pygame.sprite.spritecollide(eric, ranch_group, True):
		pygame.mixer.music.load(ranch_sounds_src[randint(0, 2)])
		pygame.mixer.music.play(1)
		eric.add_ranch()
		# Add new ranch object
		ranch = RanchSprite()
		ranch_group.add(ranch)
		score = score_font.render("Ranch Collected: " + str(eric.ranch_collected), True, (255, 0, 0))


	'''Movement Updates'''
	deltat = clock.tick(30)
	background_group.update(deltat)
	cop_group.update(deltat)
	kraft_group.update(deltat)
	ranch_group.update(deltat)
	eric.update()

	'''RENDERING'''
	screen.fill((255, 255, 255))
	background_group.draw(screen)

	screen.blit(score, (450, 22))


	# kraft_group.draw(screen)
	screen.blit(kraft_punk.src_image, (kraft_punk.position[0], kraft_punk.position[1] - 40))
	# pygame.draw.rect(screen, (255, 0, 0), kraft_punk.rect)

	# cop_group.draw(screen)
	screen.blit(cop.src_image, (cop.position[0] - 35, cop.position[1]))
	# pygame.draw.rect(screen, (255, 0, 0), cop.rect)
	
	# ranch_group.draw(screen)
	screen.blit(ranch.src_image, (ranch.position[0], ranch.position[1]))
	# pygame.draw.rect(screen, (255, 0, 0), ranch.rect)

	screen.blit(eric.src_image, (eric.position[0], eric.position[1] - 20))
	# pygame.draw.rect(screen, (255, 0, 0), eric.rect)

	pygame.display.flip()

