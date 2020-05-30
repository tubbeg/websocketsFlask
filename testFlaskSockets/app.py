from flask import Flask, render_template
from flask_socketio import *
from controller import DisplayController
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

display = DisplayController(0x3C)
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@socketio.on('messageEvent')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    message_info = json.loads(json)
    display.write_text(message_info["message"])


if __name__ == '__main__':
    socketio.run(app)
