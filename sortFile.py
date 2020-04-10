


def sortByAlphabet():

	f=open("eng_newscrawl-public_2018_1M-words.txt", "r", encoding="utf8", errors='ignore')
	Lines = f.readlines()
	
	strippedLines = [l.replace("\t"," ") for l in Lines] # remove tabs

	sortedLines = sorted(strippedLines,key=lambda x:x.split()[1]) # sort by the word in the line
	
	return sortedLines


def ChunkByLetters(Letter1,Letter2): # some reason if i choose a-c it returns a-b

	sortedWords = [w.split()[1] for w in FileSorted ] # get a list of just the words 

	index1 = sortedWords.index(Letter1)  
	index2 = len(sortedWords) - sortedWords[::-1].index(Letter2) - 1 
	print(FileSorted[index1 : index2])

	return FileSorted[index1 : index2]

def GenerateChunkFile(OutFilename):

	contents = ChunkByLetters("g","k")

	outputFile = open(OutFilename,"w",encoding="utf8") #  creates output file
	for line in contents:
		outputFile.write(line)
	outputFile.close()
	

	
FileSorted = sortByAlphabet()
GenerateChunkFile("OutFilename.txt")
