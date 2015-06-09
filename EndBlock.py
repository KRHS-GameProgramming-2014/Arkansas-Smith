import pygame

class EndBlock(pygame.sprite.Sprite):

	locked = True

	def __init__(self, pos = [0,0]):
		pygame.sprite.Sprite.__init__(self, self.containers)

		# always initialize locked endblock
		self.lock()

		self.rect = self.image.get_rect()
		self.place(pos)
		self.living = True
	
	def lock(self):
		self.image = pygame.image.load("Art/ExitBlockLocked.png")
		self.locked = True

	def unlock(self):
		self.image = pygame.image.load("Art/ExitBlockUnlocked.png")
		self.locked = False
        	
	def place(self, pos):
		self.rect.topleft = pos
		
	def update(*args):
		self = args[0]
		
		
		
		
		
		
		
		
		
		
		
		
		
