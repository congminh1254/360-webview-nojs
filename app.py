from flask import Flask, render_template, request
from configuration import get_configuration
from generate_map import generate_map
from managers.ImageProcess import ImageProcess
import json
import os.path as path
import os
import random

app = Flask(__name__, static_folder='wwwroot',
            static_url_path='/static', template_folder='templates')
app.config['FLASK_APP'] = get_configuration('flask_app')
app.config['FLASK_ENV'] = get_configuration('flask_env')

img_folder = 'data/img'
map_file = 'data/points.json'
if (path.exists(map_file) == False):
    generate_map('data')

@app.route('/')
def index():
    img = request.args.get('img')
    if img == None:
        img = random.choice(os.listdir(img_folder))
    img.replace('/', '')
    print(img)
    x = int(request.args.get('x', '180'))
    y = int(request.args.get('y', '0'))
    zoom = int(request.args.get('zoom', '120'))
    processor = ImageProcess(f'{img_folder}/'+img)
    image = processor.get_image(zoom, x, y, 720, 1080)
    image = "data:image/png;base64, "+image
    maps = json.load(open(map_file))
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != None:
                maps[i][j][0] = maps[i][j][0].replace('img/', '')
    return render_template('index.html', image=image, zoom=zoom, x=x, y=y, step=10, maps=maps, img=img)


if __name__ == '__main__':
    app.run(host=get_configuration('host'), port=get_configuration('port'))
