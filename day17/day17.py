#!/usr/bin/env python

def printNodes(startNode, findans=False):
	sd = startNode.data

	while True:
		startNode = startNode.tail

		if findans and startNode.data == findans:
			print( startNode.tail.data)
			return
		elif not findans:
			print(startNode.data,startNode.currentNode)

		if startNode.data == sd:
			print("----")
			return

def findzero(startNode):
	while True:
		if startNode.data == 0:
			return (startNode.tail.data)
		else:
			startNode = startNode.tail

class node:
	def __init__(self,data,tail=False, currentNode=False):
		self.data = data
		self.tail = tail
		self.currentNode = currentNode

puzInput=329
start = node(0)
start.tail = start
counter=1
currentNode = start

for zz in range(0,50000000):
	currentNode.currentNode = False
	for i in range(0,puzInput):
		currentNode = currentNode.tail

	currentNode.tail = node(counter, currentNode.tail, True)
	currentNode = currentNode.tail
	counter+=1

#printNodes(start,2017)
#printNodes(start)
print("number after 0:", findzero(start) )

