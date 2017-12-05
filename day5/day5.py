#!/usr/bin/python


ins = list(map(int, open("input.txt").readlines()))
#ins=[0,3,0,1,-3]
insp=0
count =  0
part2 = True


while insp < len(ins):
	t = insp
	insp = insp + ins[insp]

	if part2:
		if (ins[t] >=3):
			ins[t] = ins[t] - 1
		else:
			ins[t] = ins[t] +1
	else:
		ins[t] = ins[t] +1

	count +=1

print(ins,count)