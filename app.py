from flask import Flask, render_template, request
from configuration import get_configuration
from managers.ImageProcess import ImageProcess

app = Flask(__name__, static_folder='wwwroot',
            static_url_path='/static', template_folder='templates')
app.config['FLASK_APP'] = get_configuration('flask_app')
app.config['FLASK_ENV'] = get_configuration('flask_env')



@app.route('/')
def index():
    x = int(request.args.get('x', '0'))
    y = int(request.args.get('y', '0'))
    zoom = int(request.args.get('zoom', '120'))
    processor = ImageProcess("/Users/mcong/360-webview-nojs/data/example.jpg")
    image = processor.get_image(zoom, x, y, 720, 1080)
    image = "data:image/png;base64, "+image
    return render_template('index.html', image=image, zoom=zoom, x=x, y=y, step=10)


if __name__ == '__main__':
    app.run(host=get_configuration('host'), port=get_configuration('port'))
