#!/usr/bin/env python

import re

class particle:
	def __init__(self,pos,vel,acl):
		self.pos = pos
		self.vel = vel
		self.acl = acl
		self.s = []
		self.destroyed = False

	def update(self):
		if self.destroyed:
			return

		self.vel[0] += self.acl[0]
		self.vel[1] += self.acl[1]
		self.vel[2] += self.acl[2]
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		self.pos[2] += self.vel[2]

		self.s.append( self.distance())

	def avgdist(self):
		return sum(self.s) / len(self.s)

	def distance(self):
		return ( abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2]) )

	def __repr__(self):
		return "p=<%s>" % self.pos 


particles = []
for line in map( lambda x: x.strip(), open("input2.txt").readlines()):
	if line != "":
		m = re.search('^p=<(.*)>, v=<(.*)>, a=<(.*)>$', line)
		pos = list(map(int, m.group(1).split(","))  )
		vel = list(map(int, m.group(2).split(","))  )
		acl = list(map(int, m.group(3).split(","))  )
		particles.append( particle( pos,vel, acl) )



for i in range(100):
	for p in particles:
		p.update()

	#bad
	# use octree, but lazy, so, meh, got the answer
	for x in particles:
		for y in particles:
			if (x != y) and (not x.destroyed) and  (x.pos == y.pos):
				x.destroyed=True
				y.destroyed=True
				print("boom")

count = 0
for p in particles:
	if not p.destroyed:
		count +=1

print(count)
"""
m = False
for x in range(0, len(particles) ):
	z = particles[x].avgdist()
	if not m or z < m:
		m = z
		print(x, z)

"""