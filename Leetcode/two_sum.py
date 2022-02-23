class Solution(object):
    def twoSum(self, nums, target):
        """Given an array of integers nums and an integer target, return indices of
        two numbers such that they add up to target.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i
