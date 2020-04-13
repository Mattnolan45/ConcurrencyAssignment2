import os
from flask import Flask, request, send_file
from ChunkGenerator import *


app = Flask(__name__)
UPLOAD_FOLDER = 'D:/ConcurrencyAssignment2/UploadedFiles'
GENERATE_FOLDER = 'D:/ConcurrencyAssignment2/GeneratedFiles'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATE_FOLDER'] = GENERATE_FOLDER

generator = ChunkGenerator()


@app.route("/")
def display():
	return "<h1>Concurrent Application</h1>"


@app.route('/chunk', methods=["GET"])
def chunk():
	result = generator.ChunkByLetters(request.args.get("fileName"), request.args.get("valuePairs"))
	return result


@app.route('/Random', methods=["GET"])
def RandomGeneratedChunk():
	result = generator.GenerateRandomChunk(request.args.get("num"))
	return result


@app.route('/upload', methods=["POST"])
def uploadFile():
	f = request.files['upload_file']
	if f.filename not in os.listdir(app.config['UPLOAD_FOLDER']): 
		try:
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
			msg = "{} uploaded successfully".format(f.filename)
		except Exception as e:
			msg = "Upload failed" 
	else:
		msg = "There is already a file present with the name {}".format(f.filename)
	return msg


@app.route('/uploadedFiles',methods=["GET"])
def getUploadedFiles():
	fileList = ""
	for file in os.listdir(UPLOAD_FOLDER):
		if os.path.isfile(os.path.join(UPLOAD_FOLDER,file)):
			fileList += file+"\n"
	return fileList

@app.route('/download',methods=["GET"])
def downloadFile():
	return send_file(os.path.join(GENERATE_FOLDER, request.args.get("fileName")),as_attachment=True)



if __name__ == "__main__":
	app.run(debug=True)
	
