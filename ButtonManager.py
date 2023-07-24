import pygame

# spsro ButtonManager v1.0
# copyright songro studio_ 2020 - 2023

class Button(): # button
    def __init__(self, x, y, image, btnScale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * btnScale), int(height * btnScale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.isClicked = False

    def drawBtn(self, surface): # draw
        action = False
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked == False:
                self.isClicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.isClicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action