import pygame, Main

class playerUI:

    def renderUI(self):
        Main.screen.blit(Main.hud_HealthFull, [30, 20])
        Main.screen.blit(Main.hud_HealthFull, [65, 20])
        Main.screen.blit(Main.hud_HealthFull, [100, 20])
        Main.screen.blit(Main.icn_GunSelect_handGun, [30, 60])
        Main.screen.blit(Main.hud_bulletLeft, [66, 60])
        Main.screen.blit(Main.hud_bulletMax, [108, 60])
        Main.screen.blit(Main.hud_bulletSlash, [95, 60])