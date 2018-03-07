import numpy as np
import sys

def stringify():
	file = open("./file3.txt", "r")
	read = file.read()
	file.close()
	size = (len(read)//8)
	if len(read)%8 != 0:
		size += 1
	strs = ["" for i in range(size)]
	x = 0
	y = 0
	while x < len(read):
		if (len(read)-x) < 8:
			strs[y] = (9-(len(read)-x))*"0"+read[x:len(read)-1]
		else:
			strs[y] = read[x:(x + 8)]
		y += 1
		x += 8
	return strs

def code(string):
	H = np.matrix([
		      	  [0, 0, 1, 1, 0, 0, 0, 1,	1, 0, 0, 0, 0, 0, 0, 0, 0],
			      [1, 1, 1, 1, 0, 1, 0, 0,	0, 1, 0, 0, 0, 0, 0, 0, 0],
			      [1, 1, 0, 0, 1, 0, 0, 1,	0, 0, 1, 0, 0, 0, 0, 0, 0],
			  	  [0, 0, 1, 0, 1, 0, 1, 0,	0, 0, 0, 1, 0, 0, 0, 0, 0],
			  	  [1, 0, 1, 1, 1, 1, 0, 1,	0, 0, 0, 0, 1, 0, 0, 0, 0],
			      [0, 1, 0, 1, 1, 1, 1, 1,	0, 0, 0, 0, 0, 1, 0, 0, 0],
			      [1, 1, 1, 1, 1, 1, 1, 0,	0, 0, 0, 0, 0, 0, 1, 0, 0],
			      [0, 0, 1, 0, 1, 1, 0, 1,	0, 0, 0, 0, 0, 0, 0, 1, 0],
			      [0, 1, 0, 1, 1, 0, 1, 0,	0, 0, 0, 0, 0, 0, 0, 0, 1]
                  ])
	y = string
	for i in range(0, 9):
		x = 0
		for j in range(0, 8):
			x += int(string[j])*H[i, j]
		x = x % 2
		y += str(x)
	return y

strings = stringify()
bigstring = ""
for i in range(len(strings)):
	bigstring += code(strings[i])
file = open("./file3.txt", "w")
file.write(bigstring)
file.close()
