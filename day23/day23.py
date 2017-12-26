#!/usr/bin/env python

import string

code = list(map(lambda x: x.strip(), open("input2.txt").readlines()))
registers = {}

for a in list('abcdefgh'):
	registers[a] = 0

registers['a'] = 1
IP = 0
mulcount=0

while IP < len(code):
	
	(cmd, reg, val) = code[IP].split()

	if cmd == 'set':
		if val in string.ascii_lowercase:
			registers[reg] = registers[val]
		else:
			registers[reg] = int(val)
	elif cmd == 'sub':
		if val in string.ascii_lowercase:
			registers[reg] -= registers[val]
		else:
			registers[reg] -= int(val)
	elif cmd == 'mul':
		mulcount+=1
		if val in string.ascii_lowercase:
			registers[reg] *= registers[val]
		else:
			registers[reg] *= int(val)
	elif cmd == 'jnz':
		#print("Jump to:", val, "G:", registers['g'], "H:", registers['h'])
		if reg in string.ascii_lowercase:
			if registers[reg] !=0:
				if val in string.ascii_lowercase:
					IP += registers[val]
				else:
					IP += int(val)
				continue
		else:
			if int(reg) != 0:
				if val in string.ascii_lowercase:
					IP += registers[val]
				else:
					IP += int(val)
				continue
	IP+=1

print(registers['h'])