import pygame, sys, random
from Player1 import Player1
from Player2 import Player2
from HUD import Text
from HUD import Score
from Button import Button
from Level import Level
from Block import Block

pygame.init()

width = 800
height = 600
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("images/Screens/Start Screen.png").convert()
bgRect = bgImage.get_rect()
