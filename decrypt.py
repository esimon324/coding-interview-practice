import sys
import math
import numpy as np

def matrix_decrypt(k,str):
    rows = k
    cols = (int)(math.ceil((float)(len(str)) / (float)(k)))
    mat = np.matrix([[' ' for n in range(cols)] for m in range(rows)])
    for i in range(rows):
        for j in range(cols):
            index = (i*cols)+j
            if index < len(str):
                mat[i,j] = str[index]
    d = np.transpose(mat)
    result = ''
    for i in range(cols):
        for j in range(rows):
            result = result+d[i,j]
    return result
    
def main():
    k = (int)(sys.argv[1])
    with open('output.txt','r') as infile:
        data = infile.read()
    e = matrix_decrypt(k,data)
    with open('output.txt','w') as outfile:
        outfile.write(e)
        
if __name__ == '__main__':
    main()