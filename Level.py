import pygame, supportCSV, traceback
from tkinter import messagebox

class LevelManager:
    def __init__(self, levelData, surface):
        print('[LEVEL MANAGER] Initallizing..')
        try:
            self.displaySurf = surface
            terrainLayout = supportCSV.importCsvLayout(levelData['base'])
            
            #self.terrainSprites = self.createTileGroup(terrainLayout, 'base')
        except:
            print('[LEVEL MANAGER] Failed to initallize map!')
            print(f"{traceback.format_exc()}")
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')

    def run(self):
        pass
