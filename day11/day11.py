#!/usr/bin/env python
# https://www.redblobgames.com/grids/hexagons/

import math

cdir = {'n': (0,1,-1),
        's': (0,-1,1),
        'ne': (1,0,-1),
        'sw': (-1,0,1),
        'nw': (-1,1,0),
        'se': (1,-1,0) }

inp = "ne,ne,ne" # 3
inp = "ne,ne,sw,sw" # 0
inp = "se,sw,se,sw,sw" # 3
inp = "ne,ne,s,s" #2
inp = open("input.txt").readlines()[0].strip()


dist=[]
xx=0
yy=0
zz=0

for d in inp.split(','):
	xx = xx + cdir[d][0]
	yy = yy + cdir[d][1]
	zz = zz + cdir[d][2]
	
	dist.append(  (abs(xx) + abs(yy) + abs(zz))/2)
	

#print(x,y,  x - (y -(y%2))/2)
print((abs(xx) + abs(yy) + abs(zz))/2,  max(dist))
