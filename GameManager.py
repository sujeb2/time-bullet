import Main, pygame, sys

class Manager:
    def quitGame():
        print("Exiting..")
        pygame.quit()
        # to make sure that game is closed.
        sys.exit()

    def playSound(sound):
        pygame.mixer.Sound.play(sound)

    def pauseSound():
        pygame.mixer.music.pause()

    def unpauseSound():
        pygame.mixer.music.unpause()
