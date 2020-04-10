


def sortByAlphabet():

	f=open("eng_newscrawl-public_2018_1M-words.txt", "r",encoding="utf8", errors='ignore')
	Lines = f.readlines()
	
	strippedLines = [l.replace("\t"," ").strip() for l in Lines]

	sortedLines = sorted(strippedLines,key=lambda x:x.split()[1])
	
	return sortedLines


def ChunkByLetters(Letter1,Letter2):

	sortedWords = [w.split()[1] for w in FileSorted ]
	
	index1 = sortedWords.index(Letter1)
	
	index2 = len(sortedWords) - sortedWords[::-1].index(Letter2) - 1
	
	print(FileSorted[index1 : index2])

	
FileSorted = sortByAlphabet()
ChunkByLetters("a","c")