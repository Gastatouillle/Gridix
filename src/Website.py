from flask import Flask, request, render_template, send_from_directory
from GridGen  import *
import os

app = Flask(__name__, static_url_path='') 

FILE_DIRECTORY = 'src/files'

@app.route('/') 
def Index(): 
     return render_template('Landing.html')

@app.route('/DownloadPage', methods=['POST'])
def grid():
    space_len = request.form.get('SpaceLen', 10)
    space_wid = request.form.get('SpaceWid', 10)
    grid_min = request.form.get('GridMin', 10)
    grid_max = request.form.get('GridMax', 15)
    grid_size = GridSizer(int(grid_min), int(space_len), int(space_wid), int(grid_max))
    grids_x = CountGridsX(int(grid_size), int(space_len))
    grids_y = CountGridsX(int(grid_size), int(space_wid))

    files = os.listdir(FILE_DIRECTORY)
    thumbnails = {file: f"{file.split('.')[0]}.jpg" for file in files}
 
    return render_template('DownloadPage.html', x_units=int(grids_x), y_units=int(grids_y), files=files, thumbnails=thumbnails)

@app.route('/files/<path:filename>')
def download_file(filename):
    print(f"Requested file: {filename}")
    return send_from_directory(FILE_DIRECTORY, filename)

if __name__ == '__main__': 
    app.run()
