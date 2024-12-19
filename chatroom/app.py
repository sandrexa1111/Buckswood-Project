from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
socketio = SocketIO(app)

# Active room tracking
chat_rooms = {}  # Stores room names and their messages
active_rooms = set()  # Tracks active room names


@app.route('/')
def index():
    """Landing page for entering a chat room."""
    return render_template('index.html', rooms=list(active_rooms))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chat page where users send messages."""
    if request.method == 'POST':
        username = request.form['username']
        room = request.form['room']
        return render_template('chat.html', username=username, room=room)
    return redirect(url_for('index'))


@socketio.on('join')
def handle_join(data):
    """Handle a user joining a room."""
    username = data['username']
    room = data['room']
    join_room(room)
    send(f'{username} has joined the room.', to=room)
    chat_rooms.setdefault(room, []).append(f'{username} joined the room.')
    active_rooms.add(room)  # Add room to active list


@socketio.on('message')
def handle_message(data):
    """Handle incoming messages."""
    room = data['room']
    message = f"{data['username']}: {data['message']}"
    send(message, to=room)
    chat_rooms.setdefault(room, []).append(message)


@socketio.on('leave')
def handle_leave(data):
    """Handle a user leaving the room."""
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f'{username} has left the room.', to=room)
    chat_rooms.setdefault(room, []).append(f'{username} left the room.')
    # Remove room if empty
    if not chat_rooms[room]:
        active_rooms.discard(room)


if __name__ == '__main__':
    socketio.run(app, debug=True)
