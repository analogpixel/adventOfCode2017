#!/usr/bin/env python

import string
import math
import re
import sys
import numpy as np
from numba import jit

debug=False
fileName = "input2.txt"

## Load and permutate the rules
rules = {}
for l in map(lambda x: x.strip(), open(fileName).readlines()):
	m = re.search('(.*) => (.*)?$',l)
	r1 = "".join(m.group(1).strip().split("/"))
	r2 = "".join(m.group(2).strip().split("/"))
	r1 = np.array( [1 if c =="#" else 0 for c in r1])
	

	if len(r1) == 4:
		r1 = r1.reshape((2,2))
	else:
		r1 = r1.reshape((3,3))

	for k in range(4):
		rot = np.rot90(r1, k=k)
		tmp = "".join(['#' if c==1 else '.' for c in rot.flatten()])
		rules[tmp] = r2
		tmp = "".join(['#' if c==1 else '.' for c in np.fliplr(rot).flatten()])
		rules[tmp] = r2
		tmp = "".join(['#' if c==1 else '.' for c in np.flipud(rot).flatten()])
		rules[tmp] = r2

## Look up the correct rule and return it
def recode(x):
	return  rules[y]

## return the subcube in range with w
@jit
def getRange(cube, x,y,w):
	ret = ""
	x = int(x)
	y = int(y)
	w = int(w)

	lineW = int( math.sqrt(len(cube)))
	for i in range(w):
		t = ((y+i)*lineW)+x
		ret = ret + cube[ t:t+w ]
	return ret

## take the 4 subparts and combine back into a full cube
def combineCubes(q1,q2,q3,q4):
	lineW = int( math.sqrt(len(q1)))
	r1 = []
	r2 = []
	for i in range(lineW):
			r1 = r1 + q1[i*lineW:i*lineW+lineW] + q2[i*lineW:i*lineW+lineW]
			r2 = r2 + q3[i*lineW:i*lineW+lineW] + q4[i*lineW:i*lineW+lineW]
	return r1+r2

@jit
def getSubCubes(cube, s):
	subCubes = []
	l = len(cube)
	sideLength = int(math.sqrt(l)) # how long is each side
	cubesPerRow = int(sideLength / s) # how many cubes in each row

	for y in range(0,cubesPerRow):
		for x in range(0,cubesPerRow):
			subCubes.append( getRange(cube, x*s,y*s,s) )
	return subCubes


#cube = list('#..#........#..#')
@jit
def combineSubCubes(cubes):
	returnCube = ""
	numCubes =len(cubes)
	cubesPerRow = int(math.sqrt(numCubes))
	cubesize = int(math.sqrt(len(cubes[0])))

	#print( numCubes, cubesPerRow, cubesize)
	for i in range(0, numCubes, cubesPerRow):
		for  z in range(0, cubesize):
			for k in range(0, cubesPerRow):
				returnCube = returnCube + cubes[i+k][(z*cubesize):(z*cubesize+cubesize)]

	return returnCube

def printCube(cube):
	l = len(cube)
	sideLength = int(math.sqrt(l))
	for i in range(sideLength):
		print( "".join(cube[i*sideLength: i*sideLength+sideLength]))
	print()


cube = '.#...####'


for i in range(0,18):
	l = len(cube)
	if l % 2 == 0:
		cube = combineSubCubes(list(map(lambda x: rules[x], getSubCubes(cube,2))))
	else:
		cube = combineSubCubes(list(map(lambda x: rules[x], getSubCubes(cube,3))))
	
	print(i,len(list(filter(lambda x: x=='#', cube))))
