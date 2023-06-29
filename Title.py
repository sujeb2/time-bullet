import pygame, Main, traceback

class titleManager:
    def createTitle(title, subtitle, x, y):
        print("[TITLE MANAGER] Creating Title..")
        try:
            titleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 30)
            subtitleFont = pygame.font.Font("./src/font/PretendardVariable.ttf", 20)

            titleText = titleFont.render(title, True, (255, 255, 255))
            subtitleText = subtitleFont.render(subtitle, (255, 255, 255))

            Main.screen.blit(titleText, [x, y])
            Main.screen.blit(subtitleText, [x, y-10])
        except:
            print("[TITLE MANAGER] Error occurred while creating title.")
            print(f"[TITLE MANAGER] Traceback: {traceback.print_exc}")
