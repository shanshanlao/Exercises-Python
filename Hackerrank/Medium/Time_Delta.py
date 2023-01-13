
import math
import os
import random
import re
import sys

from datetime import datetime, timedelta
from time import strptime


def time_delta(t1, t2):
    #the input data type is string
    day1, date1, mon1, year1, time1, tz1 = t1.split(" ")
    day2, date2, mon2, year2, time2, tz2 = t2.split(" ")
    
    # Convert the month name to number
    mon1 = strptime(mon1,'%b').tm_mon 
    mon2 = strptime(mon2,'%b').tm_mon 
    
    # Convert time to datetime object
    time1 = datetime.strptime(" ".join([year1,str(mon1),date1,time1]),'%Y %m %d %H:%M:%S')
    time2 = datetime.strptime(" ".join([year2,str(mon2),date2,time2]),'%Y %m %d %H:%M:%S')
    
    # Time zone difference
    sign1 = tz1[0]
    hr1 = int(tz1[1:3])
    min1 = int(tz1[3:])

    sign2 = tz2[0]
    hr2 = int(tz2[1:3])
    min2 = int(tz2[3:])
    
    # Convert the time to UTC-time
    if sign1 == '-':
        std_time1 = time1 + timedelta(hours=hr1,minutes=min1) 
    else:
        std_time1 = time1 - timedelta(hours=hr1,minutes=min1) 

    if sign2 == '-':
        std_time2 = time2 + timedelta(hours=hr2,minutes=min2) 
    else:
        std_time2 = time2 - timedelta(hours=hr2,minutes=min2) 
    
    # Calculate the time difference
    timediff = round(abs(std_time1 - std_time2).total_seconds())
    
    return str(timediff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
