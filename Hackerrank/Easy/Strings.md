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

# What's Your Name?
```py
def print_full_name(first, last):
    print('Hello {} {}! You just delved into python.'.format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```

# Mutations 
Read a given string, change the character at a given index and then print the modified string.
```py
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string 
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```

# Find a String
Print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
```py
def count_substring(string, sub_string):
    count = 0
    
    for i in range(0,len(string)):
        test_string = string[i:i+len(sub_string)]
        if test_string == sub_string:
            count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
```

# String Validators
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
```py
if __name__ == '__main__':
    s = input()
    
    anyalnum = False
    anyalpha = False
    anydigit = False
    anylower = False
    anyupper = False
    
    for i in s:
        if i.isalnum():
            anyalnum = True
        if i.isalpha():
            anyalpha = True
        if i.isdigit():
            anydigit = True
        if i.islower():
            anylower = True
        if i.isupper():
            anyupper = True
    
    print(anyalnum, anyalpha, anydigit, anylower, anyupper, sep='\n')
```

# Text Alignment
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
```py
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    # H' as center
    # i number of 'H' on the left and right

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
```

# Text Wrap
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.
```py
import textwrap

def wrap(string, max_width):

    new_string = string[:max_width]
    
    for i in range(1,len(string)):
        if (i+max_width) % max_width == 0:
            new_slice = string[i:i+max_width]
            new_string = new_string + '\n' + new_slice
    
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```





