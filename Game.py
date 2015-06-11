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
from PushBlock import PushBlock
from KeyBlock import KeyBlock

pygame.init()

clock = pygame.time.Clock()

width = 1250
height = 750
size = width,height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("TitleAS.png")
bgRect = bgImage.get_rect()

balls = pygame.sprite.Group()
players = pygame.sprite.Group()

hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
startBlocks = pygame.sprite.Group()
endBlocks = pygame.sprite.Group()
blocks = pygame.sprite.Group()
pushblocks = pygame.sprite.Group()
keyblocks = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

PlayerBase.containers = (all, players)
BackGround.containers = (all, backgrounds)
StartBlock.containers = (all, startBlocks)
EndBlock.containers = (all, endBlocks)
Block.containers = (all, blocks)
PushBlock.containers = (all, pushblocks)
KeyBlock.containers = (all, keyblocks)
Score.containers = (all, hudItems)


#player1 = Player1([width/2, height/2])
run = False

startButton = Button([width/2, height-100],
                     "Art/Button/StartButtonAS.png",
                     "Art/Button/StartButtonAS.png")
lev = 1
while True:
    for s in all.sprites():
        s.kill()
    bgImage = pygame.image.load("TitleAS.png")
    bgRect = bgImage.get_rect()
    
    startButton = Button([width/2, height-100],
                     "Art/Button/StartButtonAS.png",
                     "Art/Button/StartButtonAS.png")
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
    level.loadLevel(lev)

    player1 = PlayerBase(startBlocks.sprites()[0].rect.center)

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
                if event.key == pygame.K_r:
                    run = False
            

        playersHitBlocks = pygame.sprite.groupcollide(players, blocks, False, False)
        playersHitPushBlocks = pygame.sprite.groupcollide(players, pushblocks, False, False)
        playersHitEnds = pygame.sprite.groupcollide(players, endBlocks, False, False)

        pushblocksHitKeyBlocks = pygame.sprite.groupcollide(pushblocks, keyblocks, False, False)
            

        for player in playersHitBlocks:
            for block in playersHitBlocks[player]:
                player.collideBlock(block)
        
        for player in playersHitPushBlocks:
            for pushblock in playersHitPushBlocks[player]:
                pushblock.collidePlayer(player)
                all.update(width, height)
                #this might introduce a noticable lag in the game when pushing push blocks...revise if you have to
                pushBlocksHitBlocks = pygame.sprite.groupcollide(pushblocks, blocks, False, False)
                for pushBlock in pushBlocksHitBlocks:
                    for block in pushBlocksHitBlocks[pushBlock]:
                        print "hitting block"
                        pushBlock.collideBlock(block) # write me to undo the last move 
                pushBlocksHitPushBlocks = pygame.sprite.groupcollide(pushblocks, pushblocks, False, False)
                for pushBlock in pushBlocksHitPushBlocks:
                    for block in pushBlocksHitPushBlocks[pushBlock]:
                        print "hitting pushblock"
                        pushBlock.collideBlock(block)
                pushBlocksHitEnds = pygame.sprite.groupcollide(pushblocks, endBlocks, False, False)
                for pushBlock in pushBlocksHitEnds:
                    for block in pushBlocksHitEnds[pushBlock]:
                        print "hitting end block"
                        pushBlock.collideBlock(block)
                pushBlocksHitPlayers = pygame.sprite.groupcollide(pushblocks, players, False, False)
                for pushBlock in pushBlocksHitPlayers:
                    for player in pushBlocksHitPlayers[pushBlock]:
                        print "hitting player"
                        player.collidePushBlock(pushBlock) # write me to undo the last move 

        
        endblock = endBlocks.sprites()[0]

        if bool(pushblocksHitKeyBlocks):
            endblock.unlock()

            for player in playersHitEnds:
                for wall in playersHitEnds[player]:
                    for obj in all.sprites():
                        obj.kill()
                    #all.update(width, height)
                    BackGround("Art/Background.png")
                    lev += 1
                    print lev, len(all.sprites())
                    level.loadLevel(lev)
                    player1 = PlayerBase(startBlocks.sprites()[0].rect.center)
        else:
            endblock.lock()

                


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
    run = True
