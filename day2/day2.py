

print ( "part 1:", sum( [max(z) - min(z) for z in  [ list(map(int,x)) for x in  [line.split() for line in open("day2.tab").readlines() ] ] ]) )


import itertools
s = 0
for a in [z for z in  [ sorted(map(int,x), reverse=True) for x in  [line.split() for line in open("day2.tab").readlines() ] ] ]:
	s += [ xz[0]/xz[1] for xz in  (filter(lambda x: x[0] % x[1]==0, itertools.permutations(a, 2)))][0] 
print("part 2:", s)