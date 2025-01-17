#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr[0])
    first = 0
    second = 0
    left = []
    row = 0
    temp = n - 1
    for i in range(n):
        left.append((row, temp))
        row += 1
        temp -= 1
    print(left)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                first += arr[i][j]
            if (i, j) in left:
                second += arr[i][j]
    return abs(first - second)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
