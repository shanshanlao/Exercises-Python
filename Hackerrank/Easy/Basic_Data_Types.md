# Find the Runner-Up Score!
Find the second largest number in the array.
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

# Nested Lists
Find all the students with the second lowest mark.
```py
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())        
        records.append([name,score])
    
    records.sort(key = lambda x:x[1])
    lowest_score = records[0][1]
    
    new_records = list(filter(lambda x:x[1]!=lowest_score, records)) 
    new_records.sort(key = lambda x:x[1])
    second_lowest = new_records[0][1]
    
    #get the students name with the second lowest score
    names = []
    for val in new_records:
        if val[1] == second_lowest:
            names.append(val[0])
            
    #sort the students' name alphabatically
    names.sort()
    
    print(*names, sep="\n")  
```

Easier way: Use set() to get the second lowest score.

**Key point: Sets does not allow duplicate values.**
```py
second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
```

# Finding the percentage
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
```py
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg_marks = sum(student_marks[query_name])/len(student_marks[query_name])
    print("{:.2f}".format(avg_marks))
```

# Lists
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
```py
if __name__ == '__main__':
    N = int(input())
    
    lst = []
    for _ in range(N):
        cmd, *arr = input().split()
        arr = list(map(int, arr))

        if cmd == 'insert':
            lst.insert(arr[0],arr[1]) 
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            lst.remove(arr[0])
        elif cmd == 'append':
            lst.append(arr[0])
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
```

# Tuples
Given an integer,n, and n space-separated integers as input, create a tuple, t , of those n integers. Then compute and print the result of hash(t).
```py
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t))
```
