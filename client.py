import requests 


while True:
	
	print("Commands : Chunk ,Random, Stop")
	text = input("Input Command: ")

	if ( text == "Chunk"):
		print("You entered: Chunk")
		val1 = input("Input Starting Letter: ")
		val2 = input("Input Finishing Letter: ")
		
		try:
			response = requests.get(
    			'http://127.0.0.1:5000/test',
    			params={'val1': val1, 'val2' : val2},
			)	
			print(response.content)
		except Exception as e:
			print("Invalid response from server")

	elif( text == "Random"):
		try:
			response = requests.get(
    			'http://127.0.0.1:5000/Random'
			)
			print(response.content)
		except Exception as e:
			print("Invalid response from server")


	elif( text == "Stop"):
		break
	else:
		print("Invalid input")