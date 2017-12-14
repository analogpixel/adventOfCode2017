#!/usr/bin/python

import sys

d = list(map(lambda x: [int(x[0].strip()), int(x[1].strip()) ], (map(lambda x: x.split(':'), open("input2.txt").readlines()))))

csum= 0
z = 0

while True:
	found=True
	for l in d:
		time  = l[0]
		depth = l[1]
		if (time+z) % ( (depth-1)*2) == 0:
			csum =  csum + (time * depth)
			found=False
			break
	if found:
		print("found at:",z)
		sys.exit()
	else:
		z +=1


#print(csum)