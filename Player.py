import pygame

class PlayerBase(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImage = pygame.image.load("ArkBack.png")
        self.downImage = pygame.image.load("Art/Arkansas Smith.png")
        self.leftImage = pygame.image.load("Art/Arkansas Smith Right.png")
        self.rightImage = pygame.image.load("Art/Arkansas Smith Left.png")
        self.facing = "up"
        self.changed = False
        self.image = self.upImage
        self.rect = self.image.get_rect()
        self.place(pos)
        self.maxSpeed = 10
        self.speedx = 0
        self.speedy = 0
    
    def place(self, pos):
        print pos
        self.rect.center = pos
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.animate()
        self.move()
        self.changed = False
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideBlock(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.move()
        self.speedx = 0
        self.speedy = 0 
    
    def collidePushBlock(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.move()
        self.speedx = 0
        self.speedy = 0 
            
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
                
    def collideWall(self, other):
        if not self.didBounceX:
            self.speedx = -self.speedx
            self.move()
            self.move()
            self.speedx = 0
            self.didBouncex = True
        if not self.didBounceY:
            self.speedy = -self.speedy
            self.move()
            self.move()
            self.move()
            self.speedy = 0
            self.didBounceY = True
            #print "hit Ball"
    
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
