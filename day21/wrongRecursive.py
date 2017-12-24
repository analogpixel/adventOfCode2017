#!/usr/bin/env python

import string
import math
import re
import sys
import numpy as np

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
	global rules
	y = "".join(x)
	return  list(rules[y])

## return the subcube in range with w
def getRange(cube, x,y,w):
	ret = []
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

## break cube into 4 sub cubes, and keep doing that
## until we get to match condition
def getCube(cube):
	if debug: print("Entering getCube with:", cube)
	if len(cube) == 4:
		if debug: print("Return Recode 2x2")
		return  recode(cube)
	if len(cube) == 9:
		if debug: print("Return Recode 3x3")
		return recode(cube)

	# how many items in each row and col
	w = math.sqrt(len(cube))

	if debug: print("getting q1-q4")
	q1 = getCube(getRange(cube,0,0, w/2))
	q2 = getCube(getRange(cube, w/2,0, w/2))
	q3 = getCube(getRange(cube, 0, w/2,w/2))
	q4 = getCube(getRange(cube, w/2,w/2,w/2))

	allCubes = combineCubes(q1,q2,q3,q4)

	if debug: print(len(q1), "q1:", q1)
	if debug: print(len(q2), "q2:", q2)
	if debug: print(len(q3), "q3:", q3)
	if debug: print(len(q4), "q4:", q4)
	if debug: print(len(allCubes), "all:", allCubes)

	return allCubes


cube = list(".#...####")
for i in range(0,5):
	cube = getCube(cube)

print(len(list(filter(lambda x: x=='#', cube))))