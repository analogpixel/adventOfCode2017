#!/usr/bin/env python



def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False


inp =  """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""



cmds = []
for l in inp.split("\n"):
	cmds.append( l.split() + ['0'] )

class prog():
	def __init__(self, cmds, prgID):
		self.cmds = cmds
		self.IP = 0
		self.output = []
		self.prgID = prgID
		self.reg = {'p': prgID}
		self.waitState = False
		self.sendQ = []
		self.RECVQ = False
		self.sndCount = 0
		self.debug = False

	def step(self):
		output = self.output
		reg = self.reg
		if self.debug: print(self.cmds[self.IP][:3])
		(cmd, var, amt) = self.cmds[self.IP][:3]

		if not var in reg:
			reg[var] = 0

		if is_digit(amt):
			amt = int(amt)
		else:
			amt= reg[amt]

		if cmd == 'snd':
			if is_digit(var):
				var = int(var)
			else:
				var = reg[var]

			if self.debug: print("sending", var)
			self.sendQ.append(var)
			self.waitState = 'snd'
			self.sndCount += 1
		
		elif cmd == 'set':
			reg[var] = amt
		
		elif cmd == 'add':
			reg[var] += amt

		elif cmd == 'mul':
			reg[var] *= amt
			
		elif cmd == 'mod':
			reg[var] = reg[var] % amt

		elif cmd == 'rcv':
			if self.debug: print(self.RECVQ)
			if len(self.RECVQ) > 0:
				amt = self.RECVQ.pop()
				if self.debug:  print("storing", amt, "in", var)
				reg[var] = amt
			else:
				self.waitState = 'rcv'
				return


		elif cmd == 'jgz':
			if reg[var] > 0:
				self.IP+=int(amt)
				return

		self.IP+=1


p1 = prog(cmds,0)
p2 = prog(cmds,1)

p1.RECVQ = p2.sendQ
p2.RECVQ = p1.sendQ

while not(p1.waitState == 'rcv' and p2.waitState == 'rcv'):
	p1.step()
	p2.step()
	#print (p1.waitState, p2.waitState)

print(p2.sndCount)
print(p1.reg, p2.reg)
