# Idea:
# If a smaller Roman numerals is placed before a larger one, subtract the small number
# For example, I can be placed before V (5) and X (10) to make 4 and 9. 

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        n = len(s)
        num = 0
        for i in range(n-1,-1,-1):
            if i!=n-1 and (romanDict[s[i]] < romanDict[s[i+1]]):
                num -= romanDict[s[i]]
            else:
                num += romanDict[s[i]]

        return num
