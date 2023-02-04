'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

# XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor = 0
        for num in nums:
            xor ^= num
        return xor
        
        # not using constant extra space ?
        # return sum(nums) - (sum(nums) - sum(set(nums)))*2
