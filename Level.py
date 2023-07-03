import pygame, CSVSupport, traceback

class Level:
    def __init__(self, level_data, surface):
        print("[LEVEL MANAGER] Initallizing..")
        try:
            self.display_surface = surface
            terrainLayout = CSVSupport.importCsvLayout(level_data['base'])
            self.terrainSprites = self.createTileGroup(terrainLayout, 'base')
        except:
            print("[LEVEL MANAGER] Error occurred while initallizing level.")
            print(f"[LEVEL MANAGER] Traceback: \n{traceback.format_exc()}")

    def createTileGroup(self, layout, type):
        print("[LEVEL MANAGER] Creating tile groups..")
        try:
            spriteGroup = pygame.sprite.Group()
            
            for row in layout:
                print(row)

            return spriteGroup
        except:
            print("[LEVEL MANAGER] Error occurred while creating tile group.")
            print(f"[LEVEL MANAGER] Traceback: \n{traceback.format_exc()}")

    def run(self): # run game / level
        pass