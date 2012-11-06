#4.13.py
# count the number of words in a sentence

import string
def main():
	sen = raw_input("Enter the sentence: ")
	words = string.split(sen)
	count = 0
	for word in words:
		count = count +1
	print "The number of words is",count
	
main()