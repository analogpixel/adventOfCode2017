#!/usr/bin/python

def parseStream(s):
	groupCount = 0
	groupLevel = 0
	score = 0
	garbageCount=0

	strm = list(s)
	i = 0
	while  i < len(strm):
		if strm[i] == "{":
			groupCount +=1
			groupLevel +=1
		if strm[i] == "}":
			score = score + groupLevel
			groupLevel -=1
		if strm[i] == "<":
			while  True:
				i = i + 1
				if strm[i] == "!":
					i = i + 1
					continue
				elif strm[i] == ">":
					break
				else:
					garbageCount +=1
		i =i + 1
	return (groupCount,score,garbageCount)


def test_ParseStream():
	assert( parseStream("{}") == (1,1,0) )
	assert( parseStream("{{{}}}") == (3,6,0) )
	assert( parseStream("{{},{}}") == (3,5,0) )
	assert( parseStream("{{{},{},{{}}}}") == (6,16,0) )
	assert( parseStream("{<{},{},{{}}>}") == (1,1,10) )
	assert( parseStream("{<a>,<a>,<a>,<a>}") == (1,1,4) )
	assert( parseStream("{{<a>},{<a>},{<a>},{<a>}}") == (5,9,4) )
	assert( parseStream("{{<!>},{<!>},{<!>},{<a>}}") == (2,3,13) )
	assert( parseStream("{{<!!>},{<!!>},{<!!>},{<!!>}}") == (5,9,0) )
	assert( parseStream('<{o"i!a,<{i<a>') == (0,0,10) )

d = open("data.txt").readlines()[0].strip()

print( parseStream(d))
