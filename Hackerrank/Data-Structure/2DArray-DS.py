def hourglassSum(arr):
    n = len(arr)
    hour_glass_sum = []
    
    for i in range(n-2): #0
        for j in range(n-2): #1,2
            theSum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            
            hour_glass_sum.append(theSum) 
    
    return max(hour_glass_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
