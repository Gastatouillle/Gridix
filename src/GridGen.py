import math

def GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize):
    MinGridSize = int(MinGridSize)
    ShelfDepth = int(ShelfDepth)
    ShelfLen = int(ShelfLen)
    MaxGridSize = int(MaxGridSize)
    
    for i in range(MinGridSize, MaxGridSize + 1):
        if ShelfDepth % i == 0 and ShelfLen % i == 0:
            return i
    return None  # Return None if no suitable grid size is found

def BedFitter(BedSize, ShelfDepth, ShelfLen, MinGridSize, MaxGridSize):
    GridSize = GridSizer(MinGridSize, ShelfDepth, ShelfLen, MaxGridSize)
    if GridSize is None:
        raise ValueError("No suitable grid size found within the given range.")
    
    ShelfDepth = int(ShelfDepth)
    ShelfLen = int(ShelfLen)
    BedSize = int(BedSize)
    
    GridsPerWidth = BedSize / GridSize
    GridsPerLength = BedSize / GridSize
    
    # Round down to leave dead space rather than overfilling
    GridsInBed = math.floor(GridsPerWidth) * math.floor(GridsPerLength)
    
    # Calculate grids needed for the entire shelf space
    GridsNeeded = (ShelfDepth / GridSize) * (ShelfLen / GridSize)
    
    # Avoid division by zero
    if GridsInBed == 0:
        raise ValueError("Bed size is too small to fit any grid units.")
    
    return GridsNeeded / GridsInBed

def CountGridsX(GridSize, ShelfLen):
    GridSize = int(GridSize)
    ShelfLen = int(ShelfLen)
    
    # Avoid division by zero
    if GridSize == 0:
        raise ValueError("Grid size cannot be zero.")
    
    return ShelfLen / GridSize

def CountGridsY(GridSize, ShelfWidth):
    GridSize = int(GridSize)
    ShelfWidth = int(ShelfWidth)
    
    # Avoid division by zero
    if GridSize == 0:
        raise ValueError("Grid size cannot be zero.")
    
    return ShelfWidth / GridSize
