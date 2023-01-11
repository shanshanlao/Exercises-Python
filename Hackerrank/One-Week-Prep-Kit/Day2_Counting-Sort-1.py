import math
import os
import random
import re
import sys

def countingSort(arr):
    
    arr.sort()
    freq_arr = [None] * 100
    
    for i in range(100):
        freq_arr[i] = arr.count(i)
        
    return freq_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
