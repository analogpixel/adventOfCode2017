#!/usr/bin/env python

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

class cmd():
	def __init__(self, cmd, reg, value=False, register=False):
		self.cmd = cmd
		self.reg = reg
		self.value = value
		self.valueIsRegister = register # is this a register

	def __repr__(self):
		if self.valueIsRegister:
			return "|%s : %s : (%s)|" % (self.cmd, self.reg, self.value) 
		else:
			return "|%s : %s : %s|" % (self.cmd, self.reg, self.value) 

class prog():
	def __init__(self, prgFile):
		self.readProgram(prgFile)
		self.IP = 0
		self.registers = {}

	def expand(self, cmd):
		t1 = cmd.cmd
		t2 = cmd.reg

		if cmd.value:
			if cmd.valueIsRegister:
				t3 = self.registers[ cmd.value ]
			else:
				t3 = cmd.value
		else:
			t3 = False

		return (t1,self.registers[t2],t3)

	def step(self):
		(cmd,reg,value) = self.expand( self.data[self.IP] )

		if cmd == 'snd':
			print("play sound", reg)
			self.lastSound = reg 
		if cmd == 'set':
			self.registers[reg] = value
		if cmd == 'add':
			self.registers[reg] += value
		if cmd == 'mul':
			self.registers[reg] *= value
		if cmd == 'mod':
			self.registers[reg] = self.registers[reg] % value
		if cmd == 'rcv':
			if reg > 0:
				print("rcv last sound:", self.lastSound)
		if cmd == 'jgz':
			if reg > 0:

	def readProgram(self,f):
		self.data = []

		for line in open(f).readlines():
			tmp = line.strip().split()
			if len(tmp) == 2:
				self.data.append( cmd(tmp[0], tmp[1]) )
			if len(tmp) == 3:
				if is_digit(tmp[2]):
					self.data.append(  cmd( tmp[0], tmp[1], int(tmp[2]), False ))
				else:
					self.data.append(  cmd( tmp[0], tmp[1], tmp[2], True) ) 




p0 = prog("p1.txt")
print(p0.data)