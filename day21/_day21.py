#!/usr/bin/env python
import re
import math

debug = True

## start state
inp = ['.','#','.',
	   '.','.','#',
       '#','#','#']

## Load the rules
rules = {}
for l in map(lambda x: x.strip(), open("input1.txt").readlines()):
	m = re.search('(.*) => (.*)?$',l)
	#print(m.group(1), m.group(2))
	rules["".join(m.group(1).strip().split("/"))] = m.group(2).strip()


l = len(inp)

for col in range( int(l/3))
