# Hello World

```py
if __name__ == '__main__':
    print("Hello, World!")
```

# Arithmetic Operators

```py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
 ```

# Division

```py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)
 ```

# Loops

```py
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)
```

# Write a function

```py
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
                
    return leap

year = int(input())
print(is_leap(year))
```

# Print
  
```py
if __name__ == '__main__':
    n = int(input())
    
    ans = ''
    
    for i in range(1,n+1):
        ans += str(i)
    
    print(ans)
```
