#!/usr/bin/env python

# pip install networkx
import networkx as nx


G = nx.Graph()

for l in open("input2.txt").readlines():
	(a,blist) = map(lambda x: x.strip(), l.split('<->'))

	inGroup=False
	blist = list(map(int,blist.split(',')))
	a = int(a)
	for n in blist:
		G.add_edge(a, n)


groups = list(nx.connected_components(G))

# answer to part 1
for g in groups:
	if 0 in g:
		print(len(g))

# answer to part 2
print( len(groups) )
