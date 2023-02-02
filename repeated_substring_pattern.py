'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(1,len(s)):
            sub_str = s[0:i]   
            sub_len = len(sub_str)       
            
            nb_sub_str = s.count(sub_str) 
            print(nb_sub_str)
            
            if nb_sub_str == 1:
                return False
            
            elif nb_sub_str*(sub_len) == len(s):
                return True
        
        return False