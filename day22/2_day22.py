#!/usr/bin/python

import numpy as np

# N = 0
# E = 1
# S = 2
# W = 3
# xmove,ymove
move = [ (0,-1), (1,0), (0,1) , (-1,0)]
curDir = 0
infectCount = 0

inp = [1 if x == '#' else 0 for x in list("".join(list(map(lambda x: x.strip(), open("input2.txt").readlines()))))]

inp = np.array(inp)
inp = np.resize(inp, (25,25))
inp = np.pad(inp, 10000, 'constant')

# find the center
x = y = cp = int(np.floor(len(inp[0])/2))

# clean 0
# weakened = 2
# infected = 1
# flagged = 3
for i in range(10000000):

	# if on clean node turn left
	if inp[y][x] == 0:
		curDir -= 1
		if curDir < 0:
			curDir = 3
		inp[y][x] = 2

	# on an infected node, turn right
	elif inp[y][x] == 1:
		curDir += 1
		if curDir > 3:
			curDir = 0
		inp[y][x] = 3

	# a weakened node
	elif inp[y][x] == 2:
		inp[y][x] = 1
		infectCount +=1

	# a flagged node
	elif inp[y][x] == 3:
		for i in range(2):
			curDir -=1
			if curDir < 0:
				curDir = 3
		inp[y][x] = 0

	# now move in direction set
	x = x + move[curDir][0]
	y = y + move[curDir][1]

	#print(inp)

print(inp)
print(infectCount)