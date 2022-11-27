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

# Print
  
```py
if __name__ == '__main__':
    n = int(input())
    
    ans = ''
    
    for i in range(1,n+1):
        ans += str(i)
    
    print(ans)
```

# If-else
```py
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n %2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
```
