


#Method reads in a file that contains n_grams in format:
#frequency word1 word2 ... word_n
#Method returns a 2D list of the words: [ [word1, word2, ... word_n], [word1, ....], ...]
#The 2D list is sorted based on the frequency of the n_grams, the most common ones at the front
#NOTE: the frequency is stored as a string (to keep the array uniform). Convert to an integer with frequency = int(n_gramList[0])
def read_N_grams(filename):
	
	n_gramList = []
	
	#open the file
	#https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
	with open(filename) as file:
		fileLines = file.readlines()
		fileLines = [x.rstrip('\n') for x in fileLines]  	#remove \n
							
	
	
	#Using the list of lines, convert each line to an array 
	for line in fileLines:
		n_gramArray = line.split()		#convert into an array of strings, split on space bar, ie "this is a string" to ["this", "is", "a", "string"]
		n_gramList.append(n_gramArray)
	
	n_gramList.sort(key=lambda x: x[0])	#sort the list based on the first string, the frequency
	
	file.close()
	return n_gramList
	




if __name__ == "__main__":
	n_gramList = read_N_grams("w5.txt")
	
	
	#print out the words as an example to see how the data is stored.
	for n_gram in n_gramList:
		printStr = ""
		for word in n_gram:
			printStr += word + " "
		print(printStr)