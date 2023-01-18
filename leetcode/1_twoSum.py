class Solution(object):
    def twoSum(self, nums, target):

        # Create a dictionary that stores 
        #   the number(key) and its index  
        twoSum = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            # if the following number's complement is 
            #    equal to any previous number
            # Retrieve its complement's index and its own index
            if complement in twoSum.keys():
                return [twoSum[complement],i]
            # If no, add the number to the dictionary
            else:
                twoSum[nums[i]] = i

        