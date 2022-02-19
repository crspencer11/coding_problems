class Solution(object):
    def maxSubArray(self, nums):
        """
        Finds contiguous subarray within array, nums, where sum of subarray is
        largest possible out of all other contiguous subarrays.
        
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        else:
            curr = 0
            maximum = 0
            for i in nums:
                curr = max(0, curr + i)
                maximum = max(curr, maximum)
            return maximum
