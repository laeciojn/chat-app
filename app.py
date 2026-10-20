from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_data(data):
    print(data)
    emit('message', data, broadcast=True) # retorna as informações ao cliente
    #broadcast -> retorna a mensagem para os clientes conectados
    ##data -> corpo da mensagem


if __name__ == '__main__':
    socketio.run(
        app,
        debug=True,
        allow_unsafe_werkzeug=True
    )