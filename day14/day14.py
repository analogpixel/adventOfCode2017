#!/usr/bin/env python

from knotHash import knotHash

inp = 'hwlqcszp'

total = 0
f = open("dataoutput.py","w")
f.write("grid = [\n")
for i in range(0,128):
	out=""
	for a in list(knotHash(inp + "-" + str(i) )):
		out = out + format(int(a,16), "04b")

	f.write( "[" + ",".join(list(out)) + "]"  )
	f.write(",\n")
	total = total + len(list(filter( lambda x: x=='1',  list(out) )))
	print(out, total)

f.write("]")

print(total)
	

