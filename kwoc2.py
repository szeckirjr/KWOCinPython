#!/usr/bin/env python3

import sys

def main():
	# Sets up input/exclude files depending on how the command line input is set up
	if(len(sys.argv)==2):
		inputfile = sys.argv[1]
	elif(sys.argv[1]=="-e"):
		inputfile = sys.argv[3]
		excludefile = sys.argv[2]
	elif(sys.argv[2]=="-e"):
		inputfile = sys.argv[1]
		excludefile = sys.argv[3]
	else:
		print("The input can not be read")
		return
	
	# Saves all lines from the file in a list	
	lines_array = read_input_file(inputfile)

	# Saves all words from the file in a list
	# Words will be all converted to lower case, unique (removing duplicates), excluded words will be removed (if any), 
	# and words will be sorted by alphabetical order
	words_array = read_words(lines_array)
	words_array = [x.lower() for x in words_array]
	words_array = remove_duplicates(words_array)
	if(len(sys.argv)==4):
		words_array = remove_excluded(words_array, excludefile)
	words_array.sort()
	max_len = find_max_len(words_array)
	print_output(words_array,lines_array,max_len)

# Find and returns the len of the longest word in a list
# By repeatedly comparing values and assigning the largest to a variable
def find_max_len(words):
	max_len = 0
	for s in words:
		if len(s)>max_len:
			max_len=len(s)
	return max_len

# Prints the output in the required format
# By going through every word and trying to find it in every line
# If word is found, count how many times it shows up
# Different outputs depending on whether count is just 1 or more than 1
def print_output(words,lines,maxlen):
	for s in words:
		line_count=1
		for l in lines:
			if(l.lower().find(s)!=-1):
				temp=l.lower().split(" ")
				count=0
				for w in temp:
					if (s==w):
						count=count+1
				space_count = maxlen+2-len(s)
				if(count>1):
					print(s.upper()+" "*space_count+l+" ("+str(line_count)+"*)")
				elif(count==1):
					print(s.upper()+" "*space_count+l+" ("+str(line_count)+")")
			line_count=line_count+1							

# Removes the excluded words from a list
# By comparing every single word to all excluded words and only saving the unique ones
def remove_excluded(words, excludefile):
	exclude_words = read_input_file(excludefile)
	exclude_words = read_words(exclude_words)
	newarray = []
	for string in words:
		if string not in exclude_words:
			newarray.append(string)
	return newarray

# Removes duplicate words from a list
# By comparing all words to previously added words and only saving those that haven't shown up before
# Also checks if word is a blank space, allowing to account for blank lines on input files
def remove_duplicates(words):
	unique = []
	for string in words:
		if string not in unique:
			if (string!=" " and string!=""):
				unique.append(string)
	return unique

# Separates the lines from an input list into specific words
# By splitting each line and extending all the words found into a new array and returning it
def read_words(input_lines):
	words = []
	for line in input_lines:
		words.extend(line.split(" "))
	return words		

# Reads a file and stores all lines in a list
# By appending every line of a file to a list and removing the new line character from the end
def read_input_file(inputfile):
	try:
		infi = open(inputfile, "r")
	except IOError:
		print("File "+inputfile+" does not exist")
		sys.exit(1)
	lines = []
	for line in infi:
		lines.append(line.strip('\n'))
	infi.close()
	return lines	

if __name__=="__main__":
	main()
