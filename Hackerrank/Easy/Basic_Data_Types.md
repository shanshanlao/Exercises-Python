# Find the Runner-Up Score!

Find the second largest number in the array

```py
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    maxN = max(arr)
    
    new_arr = list(filter(lambda a:a!=maxN, arr)) #get a new list with no max value in arr
    runner = max(new_arr)
    
    print(runner)
```
