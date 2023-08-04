import pygame, Main, GameSetting

class FadeManager:
    def redrawScreen(self):
        Main.screen.fill((255, 255, 255))
        pygame.draw.rect(Main.screen, (255, 0, 0), (200, 300, 200, 200), 0)
        pygame.draw.rect(Main.screen, (0, 255, 0), (500, 500, 100, 200), 0)

    def fadeOut(self, object):
        
        for alpha in range(0, 300):
            object.set_alpha(alpha)
            self.redrawScreen()
            Main.screen.blit(object, (0,0))
            pygame.display.update()
            pygame.time.delay(5)