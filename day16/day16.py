#!/usr/bin/env python

#lst = list('abcde')
#inp=['s1','x3/4','pe/b']

lst = list('abcdefghijklmnop')
inp = open("input2.txt").readlines()[0].strip().split(',')

past = []

for z in range(0, 30):
	if z % 1000 == 0:
		print(z)
	for i in inp:
		if i[0] == 's':
			spinSize=int(i[1:])
			lst = lst[-spinSize:] + lst[:-spinSize]

		if i[0] == 'x':
			(a,b) = map(int, i[1:].split('/'))
			tmp = lst[b]
			lst[b] = lst[a]
			lst[a] = tmp

		if i[0] == 'p':
			(a,b) = i[1:].split('/')
			x = lst.index(a)
			y = lst.index(b)
			tmp = lst[y]
			lst[y] = lst[x]
			lst[x] = tmp

	s = "".join(lst)
	past.append(s)

## Part2
# so I wrote some code that i've delete, that counts how long it takes to loop through itterations
# and that number is 30, after 30 loops, it starts over again, so the modulus of 1billion and 30 gives
# us where it will be, and then I subtract 1, since we start at 0
z = 1000000000000 % len(past) -1
print(past[9])