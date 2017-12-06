#!/usr/bin/env python

from day6 import *

def test_redist():
	assert( redist( [0,2,7,0]) == [2,4,1,2] )
	assert( redist( [2,4,1,2]) == [3,1,2,3] )
	assert( redist( [3,1,2,3]) == [0,2,3,4] )

def test_getCount():
	assert( getCount([0,2,7,0]) == (5,4) )
	assert( getCount([14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]) == (11137,1037))

