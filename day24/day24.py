#!/usr/bin/env python

def swap(l):
	tmp1 = l[0]
	tmp2 = l[1]
	return [tmp2,tmp1]

def solve(path, parts):

	# if we run out of parts
	if len(parts) == 0:
		print(len(path), ",", sum(list(map(sum,path))), ",", path)
		return 0

	#print("Path:", path)
	# get the node we need to connect to
	t = path[-1][1]
	count = 0
	for p in parts:
		# look for pieces that connect to the current last node
		if t in p:
			count+=1
			# Arrange the numbers so they touch
			np = p
			if p[0] != t:
				np = swap(p)

			removed = list(filter(lambda x: x!= p, parts))
			solve(path + [np], removed)


	if count == 0:
		print(len(path), ",", sum(list(map(sum,path))), ",", path)
		return 0


data = list(map( lambda x: list(map(int, x.strip().split('/'))), open("input2.txt").readlines()))


# find all the parts that have a zero
for p in data:
	if 0 in p:
		print("found", p)
		np = p
		if p[0] != 0:
			np = swap(p)
		
		solve(  [np],  list(filter(lambda x: x!= p, data)))



