import pygame, supportCSV, traceback, MapSetting, TileManager
from tkinter import messagebox

# spsro Level Manager v1.0
# copyright songro studio_ 2020 - 2023

class LevelManager:
    def __init__(self, levelData, surface):
        print('[LEVEL MANAGER] Initallizing..')
        try:
            self.displaySurf = surface
            self.worldShift = 0
            
            terrainLayout = supportCSV.importCsvLayout(levelData['base'])
            self.terrainSprites = self.createTileGroup(terrainLayout, 'base')
        except:
            print('[LEVEL MANAGER] Failed to initallize map!')
            print(f"[LEVEL MANAGER] {traceback.format_exc()}")
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')

    def createTileGroup(self, layout, type): # draw tile
        spriteGroup = pygame.sprite.Group()

        for rowIndex, row in enumerate(layout): # tile y pos
            for colIndex, val in enumerate(row): # tile x pos
                if val != '-1':
                    x = colIndex * MapSetting.tile_size
                    y = rowIndex * MapSetting.tile_size

                    if type == 'base':
                        try:
                            terrainTileList = supportCSV.importCutTileSheet('.\\src\\img\\map_tile\\Tileset.png')
                            tileSurface = terrainTileList[int(val)]
                            sprite = TileManager.StaticTile(MapSetting.tile_size, x, y, tileSurface)
                            sprite = TileManager.Tile(MapSetting.tile_size, x, y)
                            spriteGroup.add(sprite)
                        except:
                            print(f'[LEVEL MANAGER] Invalid terrainTileList index for value {val}')
                            print(f'[LEVEL MANAGER] {traceback.format_exc()}')

        return spriteGroup

    def run(self):
        self.terrainSprites.draw(self.displaySurf)
        self.terrainSprites.update(self.worldShift)
