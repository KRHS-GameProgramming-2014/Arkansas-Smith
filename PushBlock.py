import pygame, math
import Block

class PushBlock(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Art/Pushable Block.png")
        self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect()
        self.place(pos)
        self.living = True
        
    def collidePlayer(self, player):
        if (math.fabs(self.rect.center[0]-player.rect.center[0]+10) > 
                math.fabs(self.rect.center[1]-player.rect.center[1])):
            if player.rect.center[0] > self.rect.center[0]:
                self.rect = self.rect.move([-self.rect.width,0])
            elif player.rect.center[0] < self.rect.center[0]:
                self.rect = self.rect.move([self.rect.width,0])
        else:
            if player.rect.center[1] > self.rect.center[1]:
                self.rect = self.rect.move([0, -self.rect.height])
            elif player.rect.center[1] < self.rect.center[1]:
                self.rect = self.rect.move([0, self.rect.height])

    def place(self, pos):
        #print pos
        self.rect.topleft = pos
        
    def update(*args):
        self = args[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
