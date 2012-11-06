#4.14.py
#	calculate the average word length in a sentence

import string
def main():
	sen = raw_input("Enter the sentence: ")
	words = string .split(sen)
	count = 0
	num = 0
	for word in words:
		count = count+1
		num = num + len(word)
	ave = num/count
	print "Average word length in the sentence is",ave
	
	
main()