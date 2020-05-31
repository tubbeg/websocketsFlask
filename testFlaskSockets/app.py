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
def handle_my_custom_event(json_data):
    print('received json: ' + str(json_data))
    message_info = json_data
    display.clear_display()
    display.draw_background()
    display.draw_rectangle()
    display.write_text(message_info["message"])
    display.update_display()

if __name__ == '__main__':
    socketio.run(app)
