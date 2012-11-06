#4.11.py
#	a Caesar cipher

def main():
	text = raw_input("Enter the plaintext to encode: ")
	key = input("Enter the value of the key: ")
	msg = ""
	for ch in text:
		msg = msg + chr(ord(ch)+key)
	print "The encoded text is:",msg
	
main()