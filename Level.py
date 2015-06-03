import pygame, sys, math

from Block import Block
from StartBlock import StartBlock
from EndBlock import EndBlock


class Level():
    def __init__(self, screenSize, blockSize):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.level = ""
        
    def loadLevel(self, level):
        print level
        self.level = level
        levelFile = "maps/" + str(level) + ".lvl"
        
        f = open(levelFile, "r")
        lines = f.readlines()
        f.close()
        
        newlines = []
        
        for line in lines:
            newline = ""
            for c in line:
                if c != "\n":
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    Block([x*self.blockSize,y*self.blockSize])
                if c == "s":
                    StartBlock([x*self.blockSize,y*self.blockSize])
                if c == "e":
                    EndBlock([x*self.blockSize,y*self.blockSize])
            





\


