# 6.6.py
#	print the lyrics for five different animals

def lyric(x):
	print "Old MacDonald had a farm, Ee-igh, Ee-igh, Ee-igh, Oh!"
	print "And on that farm he had a %s, Ee-igh, Ee-igh, Oh!" % (x)
	print "With a moo, moo here and a moo, moo there."
	print "Here a moo, there a moo, everywhere a moo,moo."
	print "Old MacDonald had a farm, Ei-igh, Ee-igh, Oh!\n"
	
def main():
	lyric("cow")
	lyric("pig")
	lyric("sheep")
	lyric("monkey")
	lyric("chicken")
	
main()
	
	