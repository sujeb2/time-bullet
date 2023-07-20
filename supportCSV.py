import csv

def importCsvLayout(path):
    terrainMap = []

    with open(path) as map: # main function
        level = csv.reader(map, delimiter = ',')

        for row in level:
            terrainMap.append(list(row))
        
        return terrainMap