import argparse
import os
import sys

from flask_socketio import SocketIO
from app import create_app, socketio

parser = argparse.ArgumentParser(description='Run the Tolino frontend')
parser.add_argument('library_path', type=str, help='the path to where your epubs are stored')

args = parser.parse_args()

app = create_app(args.library_path, debug=True)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

default_port = 10964

socketio.run(app, host="0.0.0.0", port=default_port, debug=True)