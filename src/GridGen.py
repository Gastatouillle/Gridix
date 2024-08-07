import math


def GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize):
    GridSize = int(MinGridSize)
    for i in range(MinGridSize, MaxGridSize):
        ShelfDepMod = int(ShelfDepth) % GridSize
        ShelfLenMod = int(ShelfLen) % GridSize
        #determine if Gridsize divides perfectly into given space
        if ShelfDepMod == 0 and ShelfLenMod == 0:
            GridSize = i
            return i
        else:
            GridSize+=1

def BedFitter(BedSize, ShelfDepth, ShelfLen, MinGridSize, MaxGridSize):
    #Determine how many grids fit on one bed rounded down
    GridspWidth = int(BedSize)/GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize)
    GridspLen = int(BedSize)/GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize)
    #Round down to leave dead space on bed rather than overfill bed
    GridspBed = math.floor(GridspWidth) * math.floor(GridspLen)
    GridsNeeded = (int(ShelfDepth)/GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize)) * (int(ShelfLen)/GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize))

    return GridsNeeded/GridspBed

def CountGridsX(GridSize, ShelfLen):
    return ShelfLen/GridSize

def CountGridsY(GridSize, ShelfWidth):
    return ShelfWidth/GridSize