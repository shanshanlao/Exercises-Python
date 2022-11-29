# sWAP cASE
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
```py
def swap_case(s):
    
    new_str = ''
    for i in s:
        if i.islower():
            new_str = new_str + i.upper()
        else:
            new_str = new_str + i.lower()
    return new_str 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```

# String Split and Join
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
```py
def split_and_join(line):
    new_line = '-'.join(line.split(" "))
    
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```