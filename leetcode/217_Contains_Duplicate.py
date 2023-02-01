# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if len(nums) - len(unique) >= 1:
            return True      
        return False
