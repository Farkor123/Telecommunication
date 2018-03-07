import numpy as np

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

def stringify():
	file = open("./file3.txt", "r")
	read = file.read()
	file.close()
	size = (len(read)//17)
	strs = ["" for i in range(size)]
	x = 0
	y = 0
	while x < len(read):
		strs[y] = read[x:(x + 17)]
		y += 1
		x += 17
	return strs


def findErrorPosition(G, err1, err2):
    for i in range(0, 17):
        for j in range(i+1, 17):
            arr = np.matrix([[(H[0, i] + H[0, j])%2],
			                 [(H[1, i] + H[1, j])%2],
							 [(H[2, i] + H[2, j])%2],
							 [(H[3, i] + H[3, j])%2],
							 [(H[4, i] + H[4, j])%2],
							 [(H[5, i] + H[5, j])%2],
							 [(H[6, i] + H[6, j])%2],
							 [(H[7, i] + H[7, j])%2],
							 [(H[8, i] + H[8, j])%2]])
            for k in range(0, 8):
                if(arr[k, 0] != G[k, 0]):
                    break;
                if k == 7:
                    err1[0] = i
                    err2[0] = j
                    return
    return

def decode(string):
    T = np.matrix([[int(string[0])],
				   [int(string[1])],
				   [int(string[2])],
				   [int(string[3])],
				   [int(string[4])],
				   [int(string[5])],
				   [int(string[6])],
				   [int(string[7])],
				   [int(string[8])],
				   [int(string[9])],
				   [int(string[10])],
				   [int(string[11])],
				   [int(string[12])],
				   [int(string[13])],
				   [int(string[14])],
				   [int(string[15])],
				   [int(string[16])]])
    G = (H*T)%2
    err11 = np.array([-1])
    err22 = np.array([-1])
    findErrorPosition(G, err11, err22)
    err1 = err11[0]
    err2 = err22[0]
    if err1 >= 0 and err1 <= 17:
        if string[err1]==0:
            string = string[0:err1]+"1"+string[err1+1:18]
        else:
            string = string[0:err1]+"0"+string[err1+1:18]
    if err2 >= 0 and err2 <= 17:
        if string[err2]==0:
            string = string[0:err2]+"1"+string[err2+1:18]
        else:
            string = string[0:err2]+"0"+string[err2+1:18]
    return string

string = stringify()
for i in range(len(string)):
	string[i] = decode(string[i])
bigstring = ""
for j in range(len(string)):
	bigstring += string[i]
file = open("./file3.txt", "w")
file.write(bigstring)
file.close()
