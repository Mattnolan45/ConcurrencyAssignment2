from flask import Flask, render_template 
from flask_socketio import SocketIO, emit
from subprocess import Popen, PIPE, STDOUT
from time import sleep
app = Flask(__name__)

app.config['SECRET_KEY'] = "vnjgrbfnjfdk"
socketio = SocketIO(app)


@app.route('/')
def sessions():
	return render_template('index.html')

@app.route('/stream')
def stream():
	def generate():
		with open('job.log') as f:
			while True:
				yield f.read()
				sleep(1)
	return app.response_class(generate(), mimetype='text/plain')

@socketio.on('connect')
def on_connect():
	emit('my response', {'data':'Connected'})
	f=open('job.log', 'w+')
	f.write('Connected')
	f.close()

@socketio.on('disconnect')
def on_disconnect():
	emit('my response', {'data':'Disconnected'})


def messageRecieved(methods=['GET', 'POST']):
	print('Message was recieved')


@socketio.on('my event')
def handle_my_event(json, methods=['GET', 'POST']):
	print('recieved: ' + str(json))
	socketio.emit('my response', json, callback=messageRecieved)


if __name__ == '__main__':
	socketio.run(app, debug=True)