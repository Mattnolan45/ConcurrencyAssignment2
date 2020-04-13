import random, os , uuid 


class ChunkGenerator:

	def sortfile(self,filename): # add in file param

		UPLOAD_FOLDER = 'D:/ConcurrencyAssignment2/UploadedFiles' # Local folder for Uploads

		f=open(os.path.join(UPLOAD_FOLDER,filename), "r", encoding="utf8", errors='ignore')
		Lines = f.readlines()
		strippedLines = [l.replace("\t"," ") for l in Lines] # remove tabs
		return strippedLines


	def sortByAlphabet(self, filename): # sorts file alphabetically , add in file param
		strippedLines = self.sortfile(filename) # remove tabs
		sortedLines = sorted(strippedLines,key=lambda x:x.split()[1]) # sort by the word in the line
		return sortedLines


	def GenerateChunkFile(self,OutFilename, contents): # add in file location
		GENERATE_FOLDER = 'D:/ConcurrencyAssignment2/GeneratedFiles'

		outputFile = open(os.path.join(GENERATE_FOLDER, OutFilename),"w",encoding="utf8") #  creates output file
		for line in contents:
			outputFile.write(line)
		outputFile.close()


	def ChunkByLetters(self,filename,valuePairs): 

		FileSorted = self.sortByAlphabet(filename)
		sortedWords = [w.split()[1] for w in FileSorted ] # get a list of just the words 
		letters = [l[0] for l in sortedWords]
		
		
		content = ""
		TotalWords = 0
		pairs = [valuePairs[i:i+2] for i in range(0,len(valuePairs),2)]
		for pair in pairs:	
			index1 = sortedWords.index(pair[0])  
			index2 = len(sortedWords) - sortedWords[::-1].index(pair[1]) - 1 
			res = FileSorted[index1 : index2 + letters.count(pair[1])]
			TotalWords += len(res)
			content += "".join(FileSorted[index1 : index2 + letters.count(pair[1])])

		content += "Number of chunks: {} \nTotal Number of words in file: {}".format(len(pairs), TotalWords)

		unique_filename = str(uuid.uuid4().hex)+".txt" # unique filename
		self.GenerateChunkFile(unique_filename,content) # add in counts from the spec                                                  
		return unique_filename

	
	def GenerateRandomChunk(self,num): # generate random chunk using the default 
		sortedFile = self.sortfile('default.txt')
	
		content = ""
		for i in range(int(num)):
			rand1 = random.randrange(0, len(sortedFile)-2)
			rand2 = random.randrange(rand1, len(sortedFile)-1)
			content += "".join(sortedFile[rand1:rand2])

		unique_filename = str(uuid.uuid4().hex)+".txt"
		self.GenerateChunkFile(unique_filename, content) # add in counts from the spec                                                  
		return unique_filename




