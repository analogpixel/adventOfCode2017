#!/usr/bin/env python

from circularList import circularList
from functools import reduce

def knotHash(inputLengths):

	skipSize = 0
	cl = circularList(list(range(0,256)))
	inputLengths = list(map(ord, list(inputLengths))) + [17, 31, 73, 47, 23]

	for z in range(0,64):
		for l in inputLengths:
			tmpList = cl.getList(cl.getPosition() ,l)
			cl.replacePart(cl.getPosition(), list(reversed(tmpList)))
			cl.setPosition( cl.getPosition() + skipSize + l)
			skipSize +=1

	output = ''
	for i in range(0,16):
		z = reduce(lambda x,y: x^y, cl.clist[16*i:16*i+16])
		output = output +  '%02x' % z

	return output

if __name__ == "__main__":
	assert( knotHash("flqrgnkx-0") == "d4f76bdcbf838f8416ccfa8bc6d1f9e6" )
	print( knotHash("flqrgnkx-0") )