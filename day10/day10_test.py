#!/usr/bin/env python

from circularList import circularList

def test_clist():
	c = circularList([0,1,2,3,4])

	assert(c.getRealI(0) == 0 )
	assert(c.getRealI(5) == 0 )
	

	c.setPosition(6)
	assert(c.getPosition() == 1)
	c.setPosition(7)
	assert(c.getPosition() == 2)
	c.setPosition(11)
	assert(c.getPosition() == 1)

	assert( c.geti(0) == 0)
	assert( c.geti(5) == 0)
	assert( c.geti(6) == 1)
	assert( c.geti(7) == 2)

	assert( c.getList(0,3) == [0,1,2])
	
	assert( c.getList(5,3) == [0,1,2])
	assert( c.getList(1,10) == [1, 2, 3, 4, 0, 1, 2, 3, 4, 0])


