#!/usr/bin/env python

import sys



def sumXY(Matrix, x,y):
	return getXY(Matrix, x+1,y) + \
		   getXY(Matrix, x+1,y-1) + \
		   getXY(Matrix, x+1,y+1) + \
		   getXY(Matrix, x-1,y) + \
		   getXY(Matrix, x-1,y-1) + \
		   getXY(Matrix, x-1,y+1) + \
		   getXY(Matrix, x,y+1) + \
		   getXY(Matrix, x,y-1)


## return x,y of value in matrix
def getValue(Matrix, v):
	h = len(Matrix)
	w = len(Matrix[0])
	for i in range(0, len(Matrix)):
		for j in range(0, len(Matrix[0])):
			if  Matrix[i][j] == v:
				return (j - int((w/2)) ,i - int((w/2)))

def getXY(Matrix, x,y):
	h = len(Matrix)
	w = len(Matrix[0])
	x = x - int((w/2))
	y = y - int((h/2))
	return Matrix[y][x] 

def setXY(Matrix, x,y,v):
	h = len(Matrix)
	w = len(Matrix[0])
	x = x - int((w/2))
	y = y - int((h/2))
	Matrix[y][x] = v
	return Matrix

def printMatrix(m):
	for x in m:
		print(x)

def fillMatrix(Matrix, inp):
	x=0
	y=0
	n=1
	mul=1
	i =1

	Matrix = setXY(Matrix, x,y,1)
	SumMatrix = [[0 for x in range(w)] for y in range(h)] 
	SumMatrix = setXY(SumMatrix,x,y,1)

	print( getXY(SumMatrix, x,y) )

	while n < inp:
		for j in range(0,i):
			x = x +  (1 * mul)
			n = n + 1
			#print( x,y,n, )
			
			if (sumXY(SumMatrix, x,y) > 368078):
				print(sumXY(SumMatrix, x,y))
				sys.exit()

			SumMatrix = setXY(SumMatrix, x,y, sumXY(SumMatrix, x,y) )

			Matrix = setXY(Matrix,x,y, n)
			
			#if sumXY(Matrix, x,y) > 368078:
			#	print(sumXY(Matrix,x,y))
			#	sys.exit()
		for k in range(0,i):
			y = y - (1 * mul)
			n = n + 1
			#print( x,y,n,sumXY(SumMatrix, x,y))
			if (sumXY(SumMatrix, x,y) > 368078):
				print(sumXY(SumMatrix, x,y))
				sys.exit()
			SumMatrix = setXY(SumMatrix, x,y, sumXY(SumMatrix, x,y) )
			Matrix = setXY(Matrix,x,y,n)
			
			#if sumXY(Matrix, x,y) > 368078:
			#	print(sumXY(Matrix,x,y))
			#	sys.exit()

		i = i + 1
		mul = mul * -1

	return Matrix

## 371 for 368078

#(x,y) = getXY(int(sys.argv[1]))
#print(x,y)
#print(abs(x) + abs(y))

def test_fillmatrix():
	h=w=100

	Matrix    = [[0 for x in range(w)] for y in range(h)] 
	SumMatrix = [[0 for x in range(w)] for y in range(h)] 

	Matrix = fillMatrix(Matrix, 1030)
	printMatrix(Matrix)
	assert( getXY(Matrix,0,0) == 1 )
	assert( getXY(Matrix, 1,-1) == 3 )
	assert( getValue(Matrix, 1) == (0,0) )
	assert( getValue(Matrix, 10) == (2,1) )
	assert( getValue(Matrix, 12) == (2,-1) )
	assert( getValue(Matrix, 23) == (0,2) )
	assert( getValue(Matrix, 1024) == (-15,-16) )


"""
def test_ans1():
	h=w=1024

	Matrix    = [[0 for x in range(w)] for y in range(h)] 
	SumMatrix = [[0 for x in range(w)] for y in range(h)] 

	Matrix = fillMatrix(Matrix, 368078)
	(x,y) = getValue(Matrix, 368078)
	assert( abs(x) + abs(y) == 371)
"""


h=w=1024
Matrix    = [[0 for x in range(w)] for y in range(h)] 
SumMatrix = [[0 for x in range(w)] for y in range(h)] 
Matrix = fillMatrix(Matrix, 368078)
