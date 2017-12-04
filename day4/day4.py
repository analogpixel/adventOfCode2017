#!/usr/bin/env python

def test_validpass():
	assert( validpass("abcde fghij",True) == True)
	assert( validpass("abcde xyz ecdab",True) == False)
	assert( validpass("a ab abc abd abf abj",True) == True)
	assert( validpass("iiii oiii ooii oooi oooo",True) == True)
	assert( validpass("oiii ioii iioi iiio",True) == False)

def validpass(wlist, ana=False):
	words = wlist.strip().split()

	if ana:
		while(len(words) != 0):
			w1 = "".join(sorted(list(words.pop())))
			for w in words:
				if "".join(sorted(list(w))) == w1:
					return False
		return True
	else:
		if len(words) == len(set(words)):
			return True
		else:
			return False

inp = open("day4.txt").readlines()
valid = invalid = anavalid = anainvalid = 0
ana=True
for line in  inp:
	if validpass(line, ana):
		valid +=1
	else:
		invalid +=1


print("Valid:", valid, "Invalid:", invalid)
