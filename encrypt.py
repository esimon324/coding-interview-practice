import sys
import math
import numpy as np

def matrix_encrypt(k,str):
    cols = k
    rows = (int)(math.ceil((float)(len(str)) / (float)(k)))
    mat = np.matrix([[' ' for n in range(cols)] for m in range(rows)])
    for i in range(rows):
        for j in range(cols):
            index = (i*k)+j
            if index < len(str):
                mat[i,j] = str[index]   
    e = np.transpose(mat)
    result = ''
    r,c = e.shape
    for i in range(r):
        for j in range(c):
            result = result+e[i,j]
    return result
    
def main():
    k = (int)(sys.argv[1])
    with open('output.txt','r') as infile:
        data = infile.read()
    e = matrix_encrypt(k,data)
    with open('output.txt','w') as outfile:
        outfile.write(e)
        
if __name__ == '__main__':
    main()