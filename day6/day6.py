#!/usr/bin/env python

import sys

## redistribute a number to the rest of the positions in the list
def redist(x):
	count = max(x)
	i = x.index(count)
	x[i] = 0
	i += 1
	while count > 0:
		if  i > len(x)-1:
			i = 0
		x[i] = x[i] + 1
		count = count -1
		i = i + 1
	return x

## Returns (count,number of loops)
def getCount(banks):
	match = False

	ansBank = []
	ansBank.append( ",".join(map(str,banks)) )
	count = 0
	matchLoop = 0
	finalCount = 0
	
	while True:
		banks = redist(banks)
		count = count + 1

		tmp = ",".join(map(str,banks))

		# if we already have our first match
		# then check to see if we got another match
		if match:
			matchLoop+=1
			if match == tmp:
				print("LoopCount:", matchLoop)
				return (finalCount, matchLoop)
		else:
			if tmp in ansBank:
				match = tmp
				finalCount = count
				print("ans:", count)
			else:
				ansBank.append(tmp)


if __name__ == "__main__":
	print ( getCount([14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]) )
