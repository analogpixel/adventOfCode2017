#!/usr/bin/env python

tape = [0]* 10001
state = 'A'
steps=12656374
head = 5000
left = -1
right = 1

for i in range(0,steps):
	#print(head, i, state, tape)

	if state == 'A':
		if tape[head] == 0:
			tape[head] = 1
			head+=right
			state = 'B'
		else:
			tape[head] = 0
			head+=left
			state = 'C'

	elif state == 'B':
		if tape[head] == 0:
			tape[head] = 1
			head+=left
			state = 'A'
		else:
			tape[head] = 1
			head+=left
			state = 'D'

	elif state == 'C':
		if tape[head] == 0:
			tape[head] = 1
			head+=right
			state = 'D'
		else:
			tape[head] = 0
			head+=right
			state = 'C'

	elif state == 'D':
		if tape[head] == 0:
			tape[head] = 0
			head+=left
			state = 'B'
		else:
			tape[head] = 0
			head+=right
			state = 'E'

	elif state == 'E':
		if tape[head] == 0:
			tape[head] = 1
			head+=right
			state = 'C'
		else:
			tape[head] = 1
			head+=left
			state = 'F'

	elif state == 'F':
		if tape[head] == 0:
			tape[head] = 1
			head+=left
			state = 'E'
		else:
			tape[head] = 1
			head+=right
			state = 'A'
print(sum(tape))

