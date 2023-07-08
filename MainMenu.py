import pygame, Main, sys

def mainMenu():
    while Main.isMainMenu:
        for event in pygame.event.get():
            if event.type = QUIT:
                pygame.quit()
                sys.exit() # make sure that game is exited

        pygame.display.update()
        Main.clock.tick(60)
