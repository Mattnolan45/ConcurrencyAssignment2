from flask import Flask, request
from ChunkGenerator import *


app = Flask(__name__)

@app.route("/")
def display():
	return "<h1>Concurrent Application</h1>"


@app.route('/test', methods=["GET"])
def tst():
	t = ChunkGenerator.ChunkByLetters( request.args.get("val1"), request.args.get("val2"))
	return "/n".join(t)


if __name__ == "__main__":
	app.run(debug=True)
	
