#!/usr/bin/env python

import re
import string
import pdb

networkMap = []
with open("input2.txt") as f:
	line = []
	while True:
		
		c = f.read(1)

		if not c:
			networkMap.append(line)
			break

		if c == "\n":
			networkMap.append(line)
			line = []
		else:
			line.append(c)


def checkBounds(row,col, data):
	if col >= len(data[0]):
		return False

	if col < 0:
		return False

	if row >= len(data):
		return False

	if row < 0:
		return False

	return True

col = networkMap[0].index("|")
row = 0
current = "|"
colinc = 0
rowinc = 1
output = ""
steps=1

#pdb.set_trace()
while True:
	col += colinc
	row += rowinc
	steps+= 1
	
	if not checkBounds(row,col, networkMap):
		break
	
	#print("row:", row, "col:", col, networkMap[row][col])

	c = networkMap[row][col]

	if c in string.ascii_uppercase:
		#print(c)
		output = output + c
		if checkBounds(row+rowinc, col+colinc,networkMap) and not (networkMap[row+rowinc][col+colinc] in ['-','|','+']):
			print("end of puzzle")
			break
		continue

	if c == '+' and current == '|':
		if checkBounds(row,col-1 ,networkMap) and networkMap[row][col-1] in ['-'] + list(string.ascii_uppercase):
			rowinc = 0
			colinc = -1
			current = "-"
			continue
		if checkBounds(row,col+1,networkMap) and networkMap[row][col+1] in ['-'] + list(string.ascii_uppercase):
			rowinc = 0
			colinc = 1
			current = "-"
			continue

	if c == '+' and current == "-":
		if checkBounds(row-1, col,networkMap) and networkMap[row-1][col] in ['|'] + list(string.ascii_uppercase):
			rowinc = -1
			colinc = 0
			current = "|"
			continue
		if checkBounds(row+1,col,networkMap) and networkMap[row+1][col] in ['|'] + list(string.ascii_uppercase):
			rowinc = 1
			colinc = 0
			current = "|"
			continue

print(output,steps)
