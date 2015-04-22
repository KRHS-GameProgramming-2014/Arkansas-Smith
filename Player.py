import pygame

class PlayerBase(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImage = pygame.image.load("ArkansasSimth.png")
        self.downImage = pygame.image.load("ArkansasSimth.png")
        self.leftImage = pygame.image.load("ArkansasSimth.png")
        self.rightImage = pygame.image.load("ArkansasSimth.png")
    
        self.facing = "up"
        self.changed = False
        self.image = self.upImage
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 10
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
    
    def animate(self):
        if self.changed:    
            if self.facing == "up":
                self.image = self.upImage
            elif self.facing == "down":
                self.image = self.downImage
            elif self.facing == "right":
                self.image = self.rightImage
            elif self.facing == "left":
                self.image = self.leftImage
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0
