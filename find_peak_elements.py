class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        
        cur_idx = round(len(nums)/2)
        cur = nums[cur_idx]
        
        while (cur_idx < len(nums) and cur_idx >= 0):
            
            if cur_idx == len(nums) - 1:
                if cur > nums[cur_idx-1]:
                    return cur_idx
                else:
                    cur = nums[cur_idx-1]
                    cur_idx = cur_idx-1
            else:
                if cur > nums[cur_idx+1] and cur > nums[cur_idx-1]:
                    return cur_idx

                elif nums[cur_idx+1] >= cur:
                    cur = nums[cur_idx+1]
                    cur_idx = cur_idx+1

                else:
                    cur = nums[cur_idx-1]
                    cur_idx = cur_idx-1

        return cur_idx