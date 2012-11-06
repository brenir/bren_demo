#4.8.py
#	get the acronym of a phrase

import string
def main():
	phrase=raw_input("Enter the phrase: ")
	acronym = ""
	for word in string.split(phrase):
		acronym=acronym+string.capitalize(word[0])
	print "The acronym is",acronym

main()