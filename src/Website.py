from flask import Flask, request, render_template, redirect
from GridGen  import *

app = Flask(__name__, static_url_path='') 

@app.route('/') 
def Index(): 
    return render_template('Landing.html')

#

@app.route('/grid', methods=['POST'])
def grid():
    space_len = request.form.get('SpaceLen', 10)
    space_wid = request.form.get('SpaceWid', 10)
    grid_min = request.form.get('GridMin', 10)
    grid_max = request.form.get('GridMax', 15)
    grid_size = GridSizer(int(grid_min), int(space_len), int(space_wid), int(grid_max))
    grids_x = CountGridsX(int(grid_size), int(space_len))
    grids_y = CountGridsX(int(grid_size), int(space_wid))
    return render_template('Grid.html', x_units=int(grids_x), y_units=int(grids_y))

if __name__ == '__main__': 
    app.run()
