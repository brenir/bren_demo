#3.12.py
#	calculate the Gregorian Epact

def main():
	year = input("Enter a 4-digit year: ")
	c=year/100
	epact=(8+(c/4)-c+(8*c+13)/25+11*(year%19))%30
	
	print "The value of the epact of",year,"is",epact
	
main()