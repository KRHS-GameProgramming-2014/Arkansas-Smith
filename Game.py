import pygame, sys, random
from Player1 import Player1
from Player2 import Player2
from HUD import Text
from HUD import Score
from Button import Button
from Level import Level
from Block import Block

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

screen = pygame.display.set_mode(size)

run = False

startButton = Button([width/2, height-100], 
                     "Art/Button/Start_Base.png", 
                     "Art/Button/Start_Clicked.png")

while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
        bgImage = pygame.image.load("BL1.png")
        bgRect = bgImage.get_rect()
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
    while run:
        bgImage = pygame.image.load("BL1.png")
        bgRect = bgImage.get_rect()
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
        
        
