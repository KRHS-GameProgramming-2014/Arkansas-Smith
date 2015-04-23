import pygame
from Player import PlayerBase


class Player1():
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        self.image = pygame.image.load(image)
