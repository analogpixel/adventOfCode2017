#!/usr/bin/env python

class circularList:
	i = 0
	clist = False

	def __init__(self, listInput,i=0):
		self.clist = listInput
		self.i = i

	def getRealI(self,i):
		if i >= len(self.clist):
			i = i % len(self.clist)
		return i

	def setPosition(self, i):
		self.i = self.getRealI(i)

	# return the current position in the list
	def getPosition(self):
		return self.i

	# get the element at i
	def geti(self,i):
		return self.clist[self.getRealI(i)]

	def getList(self,i, x):
		ll = []
		for j in range(0,x):
			ll.append( self.geti(j+i))
		return ll

	# starting at i, replace with l
	def replacePart(self, i,l):
		for j in range(0,len(l)):
			self.clist[ self.getRealI(i+j) ] = l[j]
