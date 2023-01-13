
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.

def reverseArray(a):
    #return a[::-1] #one line solution

    n = len(a)
    new_a = [None] * n
    
    for i in range(n):
        new_a[i] = a[n-1-i]
    
    return new_a
