def findZigZagSequence(a, n):
 
    # First sort the array
    a.sort()
    
    # Get the index of the middle position
    # Change made: from (n+1) to (n-1)
    mid = int((n - 1)/2)
    
    # Move the largest number to the middle
    a[mid], a[n-1] = a[n-1], a[mid]

    # Initalize the starting and ending point as 
    # st: element after middle point
    # ed: the second-last element
    st = mid + 1
    ed = n - 2 # Change made: from n-1 to n-2 
                # because the last element was swapped with the largest number from the middle point
                # it will be the smallest number on the right side
    
    # Idea: swap all the elements between the middle point and the last element
    #       untill reaching the middle point of the right side
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



