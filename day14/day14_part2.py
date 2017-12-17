from dataoutput import grid

x=0
y=0

def ff(x,y):
	global grid
	if (x < 0):
		return
	if (x > 127):
		return
	if (y > 127):
		return
	if (y<0):
		return
	if grid[y][x] == 0:
		return

	grid[y][x] = 0

	ff(x+1,y)
	ff(x-1,y)
	ff(x,y+1)
	ff(x,y-1)
	return

count = 0
for x in range(0,128):
	for y in range(0,128):
		if grid[y][x] == 1:
			ff(x,y)
			count +=1

print(count)