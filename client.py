import requests 

def uploadFile(fileName): # upload file

	file = {'upload_file': open(fileName,'rb')}

	response = requests.post(
		'http://127.0.0.1:5000/upload',
    	files=file
	)
	print(response.content)


def chunkfile(fileName, val1, val2): # chunk file
	try:
		print("Chunking {}".format(fileName))
		response = requests.get(
    		'http://127.0.0.1:5000/chunk',
    		params={'fileName': fileName,'val1': val1, 'val2' : val2},
		)	
		print(response.content)
	except Exception as e:
		print("Invalid response from server")


def ListServerFiles(): # list all files uploaded to the server
	response = requests.get(
		'http://127.0.0.1:5000/uploadedFiles'
		)
	
	files = (response.content.decode()).split("\n")
	print("Uploaded Files on server: ")
	for f in files:
		print(f) 


def ChunkRandom(): # chunk random file
	try:
		print("Generating Random Chunk")
		response = requests.get(
    		'http://127.0.0.1:5000/Random'
		)
		print(response.content)
	except Exception as e:
		print("Invalid response from server")



# start client
while True:
	
	print("Commands : Chunk ,Random ,Upload ,Stop") # pick command
	text = input("Input Command: ")

	if ( text == "Chunk"):

		print("You entered: Chunk")
		fileChoice = input("Would you like to chunk: the Default file (command: Default), Choose file from server (command: Choose) or Upload file (command: Upload)?: ")
		
		val1 = input("Input Starting Letter: ") # value between two letters of the alphabet
		val2 = input("Input Finishing Letter: ")
		
		if( fileChoice == "Default"):
			fileName = "default.txt" # use default input
		
		elif( fileChoice == "Choose"):
			ListServerFiles()
			fileName = input("Input file name: ") # pick file from the server

		elif( fileChoice == "Upload"): # upload file
			fileName = input("Input file name to upload: ")
			uploadFile(fileName)
		else:
			print("Invalid input")

		chunkfile(fileName, val1,val2)

	elif( text == "Random"):
		ChunkRandom()

	elif( text == "Upload" ):
		fileName = input("Input file name: ")
		uploadFile(fileName)

	elif( text == "Stop"):
		break
	
	else:
		print("Invalid input")