# Given a sentence represented as an array A of strings that contains all lowercase alphabets.
# Chech if it is a pangram or not.
# A pangram is a unique sentence in which every letter of the lowercase alphabet is used at least once.

import string

class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        
        alphabets = list(string.ascii_lowercase)
        
        theDict = dict.fromkeys(alphabets, 0)
        
        allA = "".join(A)
        for i in allA:
            theDict[i] = 1
           
        if 0 in list(theDict.values()):
            return 0
        else:
            return 1
