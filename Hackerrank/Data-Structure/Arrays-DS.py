import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.

def reverseArray(a):
    #return a[::-1] #one line solution

    n = len(a)
    new_a = [None] * n
    
    for i in range(n):
        new_a[i] = a[n-1-i]
    
    return new_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
