class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
    
        while i < len(nums):
            val = target - nums[i]
            if val in nums:
                return [i,nums.index(val)]
            