from flask import Flask 

app = Flask(__name__)

@app.route("/")
def display():
	return "<h1>Concurrent Application</h1>"

#reads in the file 
def read_input():
	f=open("eng_newscrawl-public_2018_1M-words.txt", "r", encoding="utf8")

	if f.mode == 'r':
		contents = f.readlines()
		print("contents")
		print(contents[0:10])
		results = []
		for x in contents:
			results.append(x)

	init_val = input("Enter a number ")
	val_check(init_val)
	end_val = input("Enter a number ")
	val_check(end_val)


	print(results[int(init_val):int(end_val)])

#couldnt get the list to be accessible in this function in time before work
def output_stats():
	init_val = input("Enter a number ")
	val_check(init_val)
	end_val = input("Enter a number ")
	val_check(end_val)

	print(results[int(init_val):int(end_val)])


#makes sure the value taken in is a number, prob shouldnt be in this file but sure look
def val_check(x):
	try:
	   val = int(x)
	   print("Input is an integer number. Number = ", val)
	except ValueError:
	  try:
	    val = float(x)
	    print("Input is a float  number. Number = ", val)
	  except ValueError:
	      print("No.. input is not a number. It's a string")





if __name__ == "__main__":
	#app.run(debug=True)
	read_input()
	#output_stats()