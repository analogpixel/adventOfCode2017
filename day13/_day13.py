#!/usr/bin/env python
#from colorama import Fore, Back, Style, init
import sys

class firewall:
	def __init__(self):
		self.fw = {}
		self.packet = -1
		self.maxNode = 0
		self.serv = 0
		self.boom=False
		self.debug=False

	def reset(self):
		for f in self.fw:
			self.fw[f].reset()

		self.packet = -1
		self.serv=0
		self.boom=False

	def addDelay(self, delay):
		for i in range(0, delay):
			for d in self.fw:
				self.fw[d].tick()

	def addNode(self, position, depth):
		self.fw[position] = firewallNode(depth)
		if position > self.maxNode:
			self.maxNode = position


	def update(self):

		# move the packet forward one
		self.packet += 1

		# check to see if the packet hit a scanner
		if self.packet in self.fw:
			if self.fw[self.packet].position == 0:
				if self.debug: print(Back.RED, self.packet, "BOOM", Back.RESET) 
				self.boom=True
				self.serv = self.serv + (self.fw[self.packet].depth * self.packet)
				
		# update all the scanners
		for d in self.fw:
			self.fw[d].tick()

	def printFirewall(self):
		for i in range(0, self.maxNode+1):

			if i == self.packet:
				print(Fore.RED)
			else:
				print(Fore.WHITE)

			if i in self.fw:
				print(i, self.fw[i])
			else:
				print(i, '...')
		print("-----")

class firewallNode:

	def __init__(self,depth):
		self.depth = depth
		self.position=0
		self.moveDir = 1

	def reset(self):
		self.position=0
		self.moveDir=1

	def tick(self):
		self.position  += self.moveDir

		if self.position == (self.depth-1) or self.position == 0:
			self.moveDir *= -1

	def __str__(self):
		s = ""
		for i in range(0, self.depth):
			if i == self.position:
				s = s + "[S]"
			else:
				s = s + "[ ]"
		return s

def test_firewallNode():
	fwn = firewallNode(3)
	assert( fwn.depth == 3)
	assert( fwn.position == 0)
	fwn.tick()
	assert( fwn.position == 1)
	fwn.tick()
	fwn.tick()
	fwn.tick()
	assert( fwn.position== 0)


if __name__ == "__main__":
	#init() # needed for colors

	d = list(map(lambda x: [int(x[0].strip()), int(x[1].strip()) ], (map(lambda x: x.split(':'), open("input2.txt").readlines()))))
	zz = 0
	
	fw = firewall()

	for line in d:
		fw.addNode(line[0], line[1])

	while True:
		fw.addDelay(zz)

		for i in range(0,fw.maxNode+1):
			fw.update()

			if fw.boom:
				break


		if fw.debug: print(zz,fw.serv)

		if not fw.boom:
			print("Need to wait:", zz)
			break
		else:
			if zz % 1000 == 0:  print(zz)
			zz +=1
			fw.reset()

