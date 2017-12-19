#!/usr/bin/env python
import string
import sys
from queue import Queue
from threading import Thread


prg =  list(map(lambda x: x.strip().split(), open("p2.txt").readlines()))



def runProgram(prg, id, myQ, otherQ):
	registers = {'p': id }
	lastSound = False
	sndCount=0

	IP = 0
	while True:
		cmds = prg[IP]

		#if cmds[0] == 'snd':
		#	lastSound = registers[ cmds[1] ]

		if cmds[0] == 'set':
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

		elif cmds[0] == 'snd':
			sndCount+=1
			if cmds[1] in string.ascii_lowercase:
				otherQ.put( registers[cmds[1]] )
			else:
				otherQ.put( int(cmds[1]))

		elif cmds[0] == 'rcv':
			try:
				registers[cmds[1]] = myQ.get(block=True, timeout=5)
			except Exception as  e:
				print("Program", id, "snd count", sndCount, e)
				return

		elif cmds[0] == 'jgz':
			if cmds[1] in string.ascii_lowercase:
				jmp = registers[cmds[1]]
			else:
				jmp = int(cmds[1])

			if jmp > 0:
				if cmds[2] in string.ascii_lowercase:
					IP = IP + registers[cmds[2]]
				else:
					IP = IP + int(cmds[2])
				continue
		IP +=1


q0 = Queue()
q1 = Queue()

t0 = Thread(target=runProgram, args=(prg, 0, q0, q1))
t0.daemon = True

t1 = Thread(target=runProgram, args=(prg, 1,q1, q0))
t1.daemon = True

t0.start()
t1.start()

t0.join()
t1.join()

