#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    hour = s[:2]
    time = s[-2:]
    
    if time == 'PM':
        if hour == '12':
            converted_hr = hour
        else:
            converted_hr = str(int(hour) + 12)
    elif time == 'AM':
        if hour == '12':
            converted_hr = '00'
        else:
            converted_hr = hour
    
    converted_time = converted_hr + s[2:8]
    
    return converted_time
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
