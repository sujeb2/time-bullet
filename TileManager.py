import pygame, traceback
from tkinter import messagebox

# spsro Tile Manager v1.0
# copyright songro studio_ 2020 - 2023

class Tile(pygame.sprite.Sprite): # tile manager
    def __init__(self, size, x, y):
        super().__init__()
        print('[TILE MANAGER] Initallizing..')
        try:
            self.image = pygame.Surface((size, size))
            #self.image.fill('grey')
            self.rect = self.image.get_rect(topleft = (x, y))
            print('[TILE MANAGER] Initallized.')
        except:
            print('[TILE MANAGER] Error occurred while initializing tile.')
            print(f"[TILE MANAGER] {traceback.format_exc()}")
            messagebox.showerror(title='Error occurred', message=f'{traceback.format_exc()}')
        
    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
	def __init__(self, size, x, y, surface):
		super().__init__(size, x, y)
		self.image = surface
        