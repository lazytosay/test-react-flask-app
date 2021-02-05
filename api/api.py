import time
from flask import Flask
import os

app = Flask(__name__, static_folder='../build', static_url_path='/')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
