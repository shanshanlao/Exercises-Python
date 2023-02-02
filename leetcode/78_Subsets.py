'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(len(nums) + 1):
            for subset in itertools.combinations(nums,i):
                subsets.append(subset)
        
        return subsets
