import random
import os

class ChunkGenerator:

	def sortfile(self,filename): # add in file param

		UPLOAD_FOLDER = 'D:/ConcurrencyAssignment2/UploadedFiles'

		f=open(os.path.join(UPLOAD_FOLDER,filename), "r", encoding="utf8", errors='ignore')
		Lines = f.readlines()
		strippedLines = [l.replace("\t"," ") for l in Lines] # remove tabs
		return strippedLines


	def sortByAlphabet(self, filename): # sorts file alphabetically , add in file param
		strippedLines = self.sortfile(filename) # remove tabs
		sortedLines = sorted(strippedLines,key=lambda x:x.split()[1]) # sort by the word in the line
		return sortedLines


	def ChunkByLetters(self,filename,Letter1,Letter2): # some reason if i choose a-c it returns a-b
		FileSorted = self.sortByAlphabet(filename)
		sortedWords = [w.split()[1] for w in FileSorted ] # get a list of just the words 
		index1 = sortedWords.index(Letter1)  
		index2 = len(sortedWords) - sortedWords[::-1].index(Letter2) - 1 
		return FileSorted[index1 : index2] # add in counts from the spec

	def GenerateChunkFile(self,OutFilename): # add in file location
		contents = ChunkByLetters("g","k")

		outputFile = open(OutFilename,"w",encoding="utf8") #  creates output file
		for line in contents:
			outputFile.write(line)
		outputFile.close()
	

	def GenerateRandomChunk(self): # generate random chunk using the default 
		sortedFile = self.sortfile('default.txt')
		rand1 = random.randrange(0, len(sortedFile)-2)
		rand2 = random.randrange(rand1, len(sortedFile)-1)
		return sortedFile[rand1:rand2]
		


