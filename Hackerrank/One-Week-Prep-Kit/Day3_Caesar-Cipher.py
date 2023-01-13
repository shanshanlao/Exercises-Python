#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    new_str = [None] * len(s)
    
    lower_st = ord('a') 
    upper_st = ord('A') 
    
    for i in range(len(s)):
        if s[i].isalpha() == False:
            new_str[i] = s[i]
        else:
            if s[i].islower():
                new_str[i] = chr( ((ord(s[i])-lower_st) + k) % 26 + lower_st) 
            else:
                new_str[i] = chr( ((ord(s[i])-upper_st) + k) % 26 + upper_st)
    
    return "".join(new_str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
