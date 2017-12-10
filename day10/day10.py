#!/usr/bin/env python

from  functools import reduce
from circularList import circularList

if __name__ == "__main__":
	#inputLengths = [3,4,1,5]
	skipSize = 0

	#cl = circularList( list(range(0,5))  )
	#inputLengths = [3,4,1,5]

	cl = circularList(list(range(0,256)))
	inputLengths = [192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12]

	for l in inputLengths:
		tmpList = cl.getList(cl.getPosition() ,l)
		cl.replacePart(cl.getPosition(), list(reversed(tmpList)))		
		cl.setPosition( cl.getPosition() + skipSize + l)
		#print(tmpList, "\t", cl.clist, cl.getPosition(), cl.geti( cl.getPosition() ) )
		skipSize +=1

	print( cl.geti(0) * cl.geti(1) )