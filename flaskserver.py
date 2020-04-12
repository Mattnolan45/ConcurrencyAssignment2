from flask import Flask, request
from ChunkGenerator import *


generator = ChunkGenerator()

app = Flask(__name__)

@app.route("/")
def display():
	return "<h1>Concurrent Application</h1>"


@app.route('/test', methods=["GET"])
def tst():
	t = generator.ChunkByLetters( request.args.get("val1"), request.args.get("val2"))
	return "/n".join(t)


@app.route('/Random', methods=["GET"])
def RandomGeneratedChunk():
	result = generator.GenerateRandomChunk()
	return "/n".join(result)


if __name__ == "__main__":
	app.run(debug=True)
	
