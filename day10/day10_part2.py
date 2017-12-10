#!/usr/bin/env python

from circularList import circularList
from functools import reduce

import sys

def listToAscii(l):
	return list(map(ord, list(",".join(map(str, l))))) + [17, 31, 73, 47, 23]

if __name__ == "__main__":

	skipSize = 0
	cl = circularList(list(range(0,256)))
	inputLengths = [192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12]
	inputLengths = listToAscii(inputLengths)

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
	print(output)