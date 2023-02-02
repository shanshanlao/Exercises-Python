'''
Write a function:

  def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
'''

def solution(A):
    # Remove negative numbers in the list
    A = list(filter(lambda x:x>0, A))

    # If A contains all negative numbers
    if len(A) == 0:
        return 1
    
    # Sort the positive A list
    A.sort()
    maxN = max(A)

    # Remove duplicates
    A = list(set(A))
    B = range(1,maxN+1)

    # If setA has the same length with array[1,2,..maxN]
    # that means nothing missing in between
    if len(A) == len(B):
        return maxN + 1
    else:
        for i in range(maxN):
            if A[i] != i+1:
                return i+1 

