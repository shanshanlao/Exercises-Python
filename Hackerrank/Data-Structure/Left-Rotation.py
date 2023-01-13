
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr

def rotateLeft(d, arr):
    n = len(arr)
    new_arr = [None] * n
    
    for i in range(n):
        if i >= d:
            new_arr[i-d] = arr[i]
        else:
            new_arr[n-(d-i)] = arr[i]
  
    return new_arr


