import numpy as np
import sys

H = np.matrix([[1,1,1,1,1,0,1,0,1,0,0,0,0,0],
			   [1,1,1,1,0,1,1,0,0,1,0,0,0,0],
			   [1,1,1,0,1,1,1,0,0,0,1,0,0,0],
			   [1,1,0,1,1,1,0,1,0,0,0,1,0,0],
			   [1,0,1,1,1,1,0,1,0,0,0,0,1,0],
			   [0,1,1,1,1,1,0,1,0,0,0,0,0,1]])

def findErrorPosition(x, y):
    for i in range(0, 14):
        for j in range(0,6):
            if x[j,i] != y[j,0]:
                break;
            else:
                if j == 5:
                    return i
    return -1

def decode():
    f = open("./file2.txt", "r")
    a = f.read()
    f.close()
    print(a)
    T = np.matrix([[int(a[0])],[int(a[1])],[int(a[2])],[int(a[3])],[int(a[4])],[int(a[5])],[int(a[6])],[int(a[7])],[int(a[8])],[int(a[9])],[int(a[10])],[int(a[11])],[int(a[12])],[int(a[13])]])
    G = (H*T)%2
    print(H)
    print(G)
    i = findErrorPosition(H, G)
    print(i)
    if i >= 0 and i <= 13:
        if T[i]==0:
            T[i] = 1
            b = a[0:i]+"1"+a[i+1:14]
        else:
            T[i] = 0
            b = a[0:i]+"0"+a[i+1:14]
        return b
    else:
        return a


print(decode())
