inp = list(open("input1.txt").readlines()[0].strip())

jmp=1
print( "Part1:", sum([ int(inp[x]) for x in filter( lambda x: inp[x] == inp[ int((x+jmp) % len(inp)) ], range(len(inp)) ) ] )) 

jmp = int(len(inp)/2)
print( "Part2:", sum([ int(inp[x]) for x in filter( lambda x: inp[x] == inp[ int((x+jmp) % len(inp)) ], range(len(inp)) ) ] )) 


