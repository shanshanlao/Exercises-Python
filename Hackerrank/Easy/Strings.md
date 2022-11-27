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
