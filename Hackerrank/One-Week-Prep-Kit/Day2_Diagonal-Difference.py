#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    n = len(arr)
    
    primary = 0
    second = 0
    for i in range(n):
        primary = primary + arr[i][i]
        second = second + arr[i][n-1-i]
         
    return abs(primary - second)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
