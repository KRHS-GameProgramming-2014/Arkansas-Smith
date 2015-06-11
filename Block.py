import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load("Art/Block.png")
		self.image = pygame.transform.scale(self.image, [size,size])
		self.rect = self.image.get_rect()
		self.place(pos)
		self.living = True
		
	def place(self, pos):
		#print pos
		self.rect.topleft = pos
		
	def update(*args):
		self = args[0]
		
		
		
		
		
		
		
		
		
		
		
		
		
		
