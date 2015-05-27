import pygame, sys, random
from Player import PlayerBase
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from StartBlock import StartBlock
from EndBlock import EndBlock
from Block import Block

pygame.init()

clock = pygame.time.Clock()

width = 1250
height = 750
size = width,height



screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Art/BackupBackgroundThanks Gage.png")
bgRect = bgImage.get_rect()

balls = pygame.sprite.Group()
players = pygame.sprite.Group()


hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
startBlocks = pygame.sprite.Group()
endBlocks = pygame.sprite.Group()
blocks = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

PlayerBase.containers = (all, players)
BackGround.containers = (all, backgrounds)
StartBlock.containers = (all, startBlocks)
EndBlock.containers = (all, endBlocks)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)

level = Level(size, 30)
lev = 1
level.loadLevel(lev)
player = Player(startBlocks.sprites()[0].rect.center)

#player1 = Player1([width/2, height/2])
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

        bgColor = r,g,b = 0,12,50
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)

    BackGround("Art/Background.png")

    level = Level(size, 60)
    level.loadLevel("1")

    player1 = PlayerBase([width/2, height/2])

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6

    score = Score([width-80, height-25], "Score: ", 36)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.go("up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.go("right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.go("down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.go("stop left")

        playersHitBlocks = pygame.sprite.groupcollide(players, blocks, False, False)
        
        for player in playersHitBlocks:
            for block in playersHitBlocks[player]:
                player.collideBlock(block)
                          
        if timerWait < timerWaitMax:
            timerWait += 1
        else:
            timerWait = 0
            timer.increaseScore(.1)
        
        all.update(width, height)
        
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
