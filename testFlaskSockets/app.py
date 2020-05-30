from flask import Flask, render_template
from flask_socketio import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@socketio.on('messageEvent')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app)
