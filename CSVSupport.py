from csv import reader

def importCsvLayout(path): # load map csv file format
    print("[LEVEL IMPORTER] Importing..")
    try:
        terrainMap = []

        with open(path) as map:
            level = reader(map, delimiter=',')
            for row in level:
                terrainMap.append(list(row))
    except:
        print("[LEVEL IMPORTER] Error occurred while importing level.")