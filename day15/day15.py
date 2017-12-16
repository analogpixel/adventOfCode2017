#!/usr/bin/env python

# create a simple generator so you can just call next to get the next
# number in the series.
# return only the last 16bits because that's all you care about
def gen(nextx, factorx, n):
	while True:
		nextx =  (nextx * factorx) % 2147483647
		if nextx % n == 0:
			yield nextx & 0xFFFF


#
# Part 1
#
## create the generators 
A = gen(516, 16807,1)
B = gen(190,48271,1)


## get 40,000,000 pairs of numbers from the generators, and sum up
# how many are true
print("part1:", sum([ next(A) == next(B) for x in range(40000000)]))

#
# Part 2
#
## create the generators 
A = gen(516, 16807,4)
B = gen(190,48271,8)


## get 5,000,000 pairs of numbers from the generators, and sum up
# how many are true
print("part2:", sum([ next(A) == next(B) for x in range(5000000)]))

