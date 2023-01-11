
import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    
    for n in arr:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
            
    total = len(arr)
    
    print(round(pos/total,6))
    print(round(neg/total,6))
    print(round(zero/total,6))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
