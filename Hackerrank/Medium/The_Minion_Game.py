def minion_game(string):
    
    n = len(string)
    vowels = ['A','E','I','O','U']
    
    score_stuart = 0
    score_kevin = 0
    
    # for every element X at index i, 
    # it has (n-i) possible substrings starts from index i
    
    # For example, element at index 1 in a string with length 5 will have substring:
    # str[1:2], str[1:3], str[1:4], str[1:5]
    # altogether we get (5-1)=4 substrings
    for i in range(n):
        if string[i] in vowels:
            score_kevin += n - i 
        else:
            score_stuart += n - i

    if score_stuart < score_kevin:
        print('Kevin',score_kevin)
    elif score_stuart == score_kevin:
        print('Draw')
    else:
        print('Stuart',score_stuart)
        
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
