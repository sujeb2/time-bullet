import csv, pygame, MapSetting

# spsro CSV File format supporter v1.0
# copyright songro studio_ 2020 - 2023

def importCsvLayout(path): # support csv
    terrainMap = []

    with open(path) as map: # main function
        level = csv.reader(map, delimiter = ',')

        for row in level:
            terrainMap.append(list(row))
        
        return terrainMap
    
def importCutTileSheet(path): # cut tilesheet and apply
    surface = pygame.image.load(path).convert_alpha()
    tileNumX = int(surface.get_size()[0] / MapSetting.tile_size)
    tileNumY = int(surface.get_size()[1] / MapSetting.tile_size)

    cutTiles = []

    for row in range(tileNumY):
        for col in range(tileNumX):
            x = col * MapSetting.tile_size
            y = row * MapSetting.tile_size
            newSurface = pygame.Surface((MapSetting.tile_size, MapSetting.tile_size))
            newSurface.blit(surface, (x, y), pygame.Rect(x, y, MapSetting.tile_size, MapSetting.tile_size))
            cutTiles.append(newSurface)

    return cutTiles