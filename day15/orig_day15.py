#!/usr/bin/env python

nextA=516
nextB=190

#nextA=65 # demoinput
#nextB=8921 #demoinput

factorA=16807
factorB=48271

count=0
pair=0

aQ = []
bQ = []

#for i in range(0,40000000): # part 1
#for i in range(0,5000000):
while pair <= 5000000:
	nextA =  (nextA * factorA) % 2147483647
	nextB =  (nextB * factorB) % 2147483647


	if nextA % 4 == 0:	
		aQ.append(bin(nextA)[-16:])

	if nextB % 8 == 0:
		bQ.append(bin(nextB)[-16:])

	while len(aQ) > 0 and len(bQ) > 0:
		str1 = aQ.pop(0)
		str2 = bQ.pop(0)
		pair = pair + 1

		if str1 == str2:
			count = count + 1
			print(pair, count)

print(count)

