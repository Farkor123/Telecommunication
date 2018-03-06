import numpy as np
import sys

H = np.matrix([[0,1,1,1,1,0,0,1,1,0,0,0],[1,0,1,1,0,0,1,1,0,1,0,0],[0,1,1,0,1,1,1,1,0,0,1,0],[1,0,0,1,1,1,1,1,0,0,0,1]])

def findErrorPosition(x, y):
    for i in range(0, 12):
        if (y==x[:,i]).all(0):
            return i
def decode():
    a = str(sys.argv[1])
    T = np.matrix([[int(a[1])],[int(a[1])],[int(a[2])],[int(a[3])],[int(a[4])],[int(a[5])],[int(a[6])],[int(a[7])],[int(a[8])],[int(a[9])],[int(a[10])],[int(a[11])]])
    print(T.getT())
    G = (H*T)%2
    i = findErrorPosition(H, G)
    if T[i]==0:
        T[i] = 1
    else:
        T[i] = 0
    return T

print(decode().getT())
