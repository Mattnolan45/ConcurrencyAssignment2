import os
from flask import Flask, request
from ChunkGenerator import *


app = Flask(__name__)
UPLOAD_FOLDER = 'D:/ConcurrencyAssignment2/UploadedFiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



generator = ChunkGenerator()



@app.route("/")
def display():
	return "<h1>Concurrent Application</h1>"


@app.route('/chunk', methods=["GET"])
def tst():
	t = generator.ChunkByLetters(request.args.get("fileName"), request.args.get("val1"), request.args.get("val2"))
	return "/n".join(t)


@app.route('/Random', methods=["GET"])
def RandomGeneratedChunk():
	result = generator.GenerateRandomChunk()
	return "/n".join(result)


@app.route('/upload', methods=["POST"])
def uploadFile():
	f = request.files['upload_file']
	try:
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		msg = "{} uploaded successfully".format(f.filename)
	except Exception as e:
		msg = "Upload failed" 
	return msg


@app.route('/uploadedFiles',methods=["GET"])
def getUploadedFiles():
	fileList = ""
	for file in os.listdir(UPLOAD_FOLDER):
		if os.path.isfile(os.path.join(UPLOAD_FOLDER,file)):
			fileList += file+"\n"
	return fileList



if __name__ == "__main__":
	app.run(debug=True)
	
