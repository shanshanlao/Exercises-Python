'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
          
            i = j
            # if current ele is not zero, move to the next index
            if nums[i] != 0:
                j = i+1
                
            # if the current ele is zero, 
            # move the whole array up one index 
            # and set the last telement as 0
            else:
                nums[i:n-1] = nums[i+1:]
                nums[-1] = 0
                j = i               # reset index to the current index
            

''' Faster Solution '''
# If the element is not zero, move j to the next element
# bascially using j as an indicator (or thinking about it as a new array)
# putting the new non-zero element to position j
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            
            
            
