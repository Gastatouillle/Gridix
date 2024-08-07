from flask import Flask, request, render_template 
from src.GridGen  import *

app = Flask(__name__) 
  
@app.route('/Landing', methods=['GET', 'POST']) 
def GetData(): 
    if request.method == 'POST': 
        global GridSize
        global ShelfLen
        global ShelfWidth
        MinimumGridSize = int(request.form.get('MinimumGridSizeInput'))
        MaximumGridSize = int(request.form.get('MaximumGridSizeInput'))
        ShelfLen = int(request.form.get('ShelfLenInput'))
        ShelfWidth = int(request.form.get('ShelfWidthInput'))
        BedSize = request.form.get('BedSizeText')
        GridSize = GridSizer(MinimumGridSize, ShelfWidth, ShelfLen, MaximumGridSize)
        
        print(f"Gridsize is: {GridSize}")
    
    return render_template('Landing.html')

@app.route('/Grid')
def CreateLayout():
    CountGridsX(GridSize, ShelfWidth)
    CountGridsY(GridSize, ShelfLen)
    return render_template('Grid.html')

if __name__ == '__main__': 
    app.run()