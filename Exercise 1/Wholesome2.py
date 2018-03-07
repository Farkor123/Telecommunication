import numpy as np
from types import *
import sys

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

def code():
    f = open("./file2.txt","w")
    a = str(sys.argv[1])
    f.write(a)
    for i in range(0, 9):
	    x = 0
	    for j in range(0,8):
		    x = x + int(a[j]) * H[i,j]
	    x = x%2
	    f.write(str(x))
    f.close()
    d = open("./file2.txt","r+")
    print(d.read())
    d.close()

def createError():
    f = open("./file2.txt","r")
    inp = input("Ktory bit zmienic?\n")
    a = f.read()
    f.close()
    b = a[0:int(inp)]+str((int(a[int(inp)])+1)%2)+a[int(inp)+1:len(a)]
    print(b)
    f = open("./file2.txt","w")
    f.write(b)
    f.close()
    f = open("./file2.txt","r")
    inp = input("Ktory bit zmienic?\n")
    a = f.read()
    f.close()
    b = a[0:int(inp)]+str((int(a[int(inp)])+1)%2)+a[int(inp)+1:len(a)]
    print(b)
    f = open("./file2.txt","w")
    f.write(b)
    f.close()

def findErrorPosition(y, err1, err2):
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
                if(arr[k, 0] != y[k, 0]):
                    break;
                if k == 7:
                    err1[0] = i
                    err2[0] = j
                    return
    return

def decode():
    f = open("./file2.txt","r+")
    a = f.read()
    f.close()
    T = np.matrix([[int(a[0])],
				   [int(a[1])],
				   [int(a[2])],
				   [int(a[3])],
				   [int(a[4])],
				   [int(a[5])],
				   [int(a[6])],
				   [int(a[7])],
				   [int(a[8])],
				   [int(a[9])],
				   [int(a[10])],
				   [int(a[11])],
				   [int(a[12])],
				   [int(a[13])],
				   [int(a[14])],
				   [int(a[15])],
				   [int(a[16])]])
    G = (H*T)%2
    err11 = np.array([-1])
    err22 = np.array([-1])
    findErrorPosition(G, err11, err22)
    err1 = err11[0]
    err2 = err22[0]
    if err1 >= 0 and err1 <= 17:
        if T[err1]==0:
            T[err1] = 1
            a = a[0:err1]+"1"+a[err1+1:18]
        else:
            T[err1] = 0
            a = a[0:err1]+"0"+a[err1+1:18]
    if err2 >= 0 and err2 <= 17:
        if T[err2]==0:
            T[err2] = 1
            a = a[0:err2]+"1"+a[err2+1:18]
        else:
            T[err1] = 0
            a = a[0:err2]+"0"+a[err2+1:18]
        print("Poprawny kod to\n",a)

code()
createError()
decode()
