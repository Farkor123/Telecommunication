import numpy as np
import sys

H = np.matrix([[0,1,1,1,1,0,0,1,1,0,0,0],
               [1,0,1,1,0,0,1,1,0,1,0,0],
               [0,1,1,0,1,1,1,1,0,0,1,0],
               [1,0,0,1,1,1,1,1,0,0,0,1]])

def code():
    a = str(sys.argv[1])
    f = open("./file.txt","w")
    f.write(a)
    for i in range(0, 4):
	    x = 0
	    for j in range(0,8):
		    x = x + int(a[j]) * H[i,j]
	    x = x%2
	    f.write(str(x))
    f.close()

def createError():
    f = open("./file.txt","r")
    a = f.read()
    f.close()
    print(a)
    inp = input("Ktory bit zmienic?\n")
    b = a[0:int(inp)]+str((int(a[int(inp)])+1)%2)+a[int(inp)+1:len(a)]
    print(b)
    f = open("./file.txt","w")
    f.write(b)
    f.close()

def findErrorPosition(x, y):
    for i in range(0, 12):
        for j in range(0,4):
            if x[j,i] != y[j,0]:
                break;
            else:
                if j == 3:
                    return i
    return -1

def decode():
    f = open("./file.txt", "r")
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
                   [int(a[11])]])
    G = (H*T)%2
    i = findErrorPosition(H, G)
    if i >= 0 and i <= 11:
        if T[i]==0:
            T[i] = 1
            a = a[0:i]+"1"+a[i+1:12]
        else:
            T[i] = 0
            a = a[0:i]+"0"+a[i+1:12]
        return a

code()
createError()
print("Poprawna wiadomosc to:\n",decode())
