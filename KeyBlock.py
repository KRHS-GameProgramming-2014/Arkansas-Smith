import pygame, math
import Block

class KeyBlock(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Art/KeyBlock.png")
        self.image = pygame.transform.scale(self.image, [20,20])
        self.rect = self.image.get_rect()
        self.place(pos)
        self.living = True
        
    def place(self, pos):
        #print pos
        self.rect.center = pos
        
    def update(*args):
        self = args[0]
		
		
		
		
		
		
		
		
