#!/usr/bin/env python
import string
import sys

registers = {'p': 0 }
lastSound = False

prg =  list(map(lambda x: x.strip().split(), open("p2.txt").readlines()))

print(prg)
IP = 0
while True:
	cmds = prg[IP]

	if cmds[0] == 'snd':
		lastSound = registers[ cmds[1] ]

	elif cmds[0] == 'set':
		if cmds[2] in string.ascii_lowercase:
			registers[cmds[1] ] = registers[cmds[2]]
		else:
			registers[cmds[1]]  = int(cmds[2])

	elif cmds[0] == 'add':
		if cmds[2] in string.ascii_lowercase:
			registers[cmds[1]] += registers[cmds[2]]
		else:
			registers[cmds[1]] += int(cmds[2])

	elif cmds[0] == 'mul':
		if cmds[2] in string.ascii_lowercase:
			registers[cmds[1]] *= registers[cmds[2]]
		else:
			registers[cmds[1]] *= int(cmds[2])

	elif cmds[0] == 'mod':
		if cmds[2] in string.ascii_lowercase:
			registers[cmds[1]] = registers[cmds[1]] % registers[cmds[2]]
		else:
			registers[cmds[1]] = registers[cmds[1]] % int(cmds[2])

	elif cmds[0] == 'rcv':
		if registers[cmds[1]]> 0:
			print("Last Sound:", lastSound)
			sys.exit()

	elif cmds[0] == 'jgz':
		if registers[cmds[1]] > 0:
			if cmds[2] in string.ascii_lowercase:
				IP = IP + registers[cmds[2]]
			else:
				IP = IP + int(cmds[2])
			continue
	IP +=1


