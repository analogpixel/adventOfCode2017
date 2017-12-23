#!/usr/bin/env python
import re
import math

debug = True

## start state
inp = ['.','#','.',
	   '.','.','#',
       '#','#','#']
"""
inp = ['.','#','.','.','#','.',
	   '.','.','#','.','#','.',
       '#','#','#','.','#','.',
       '.','#','.','.','#','.',
	   '.','.','#','.','#','.',
       '#','#','#','.','#','.']
"""
# given the top corner and size of square
# return flattened section
# 0 0
# 1 1 
# flatten(0,0,2) = 0011
def flatten(startRow,startCol,cubeSize,inp):
	l = len(inp)
	# each cube of cubeSize has cubesize^2 numbers so how many cubes?
	numSection = int(l/(cubeSize * cubeSize))
	if debug: print("NumSection:", numSection)

	# number of cubeSize X cubeSize boxes
	width = height = int(math.sqrt(numSection))
	if debug: print("width:", width, "height:", height)

	# how long is each line
	lineLenght = int(l / (width * cubeSize))
	if debug: print("lineLenght:", lineLenght)

	strOut = ""
	for row in range(0,3):
		for col in range(0,3):
				# get all the values in the cube
				z = ( startCol + (lineLenght*row) + col + (startRow *lineLenght) )
				if debug: print(z)
				strOut += inp[z] 

	return strOut

# inp = [ [...], [...], [....] ]
def buildCubes(inp,cubeSize):
	ret = ""
	i = 0
	l = len(inp[0])
	#print("inplen:", len(inp[0]) )
	#for row in range(math.sqrt(l)):
	#	for col in range(math.sqrt(l)):

	while i < len(inp[0]):
		if debug: print("i",i)
		for x in inp:
			for k in (range(i, i+cubeSize) ):
				ret = ret + x[k]
		i = i + cubeSize
		ret = ret + "/"
	return ret

## Load the rules
rules = {}
for l in map(lambda x: x.strip(), open("input1.txt").readlines()):
	m = re.search('(.*) => (.*)?$',l)
	#print(m.group(1), m.group(2))
	rules["".join(m.group(1).strip().split("/"))] = m.group(2).strip()


l = len(inp)

if  l % 3 == 0:
	z = flatten(0,0,3,inp)
	newbox = rules[z].split('/')
	print("converted:", newbox)
	#print("flatten:", buildCubes(newbox,2))
else:
	pass
