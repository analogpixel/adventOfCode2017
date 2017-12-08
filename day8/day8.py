#!/usr/bin/env python

import re

registers = {}


checks = {
	">": lambda x,y: x > y,
	">=": lambda x,y: x >= y,
	"<=": lambda x,y: x <= y,
	"<": lambda x,y: x < y,
	"==": lambda x,y: x == y,
	"!=": lambda x,y: x != y,
}

code = list(map(lambda x: x.strip(), open("input2.txt").readlines()))

max = 0

for line in code:
	(reg,cmd,amt,_if,regcon1, checkType, checkamt) = line.split()
	amt = int(amt)
	checkamt = int(checkamt)

	if not reg in registers:
		registers[reg] = 0
	if not regcon1 in registers:
		registers[regcon1] = 0

	if checks[checkType](registers[regcon1], checkamt):
		if cmd == "inc":
			registers[reg] = registers[reg] + amt
			
		if cmd == "dec":
			registers[reg] = registers[reg] - amt

		if abs(registers[reg]) > max:
				max = abs(registers[reg])
				
print("all time high:", max)

max = False
maxr = ""
for x in registers:
	if not max:
		max = registers[x]
		maxr = x

	if max < registers[x]:
		max = registers[x]
		maxr = x

print (max,maxr)