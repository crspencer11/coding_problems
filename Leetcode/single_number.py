class Solution(object):
    def singleNumber(self, nums):
        """Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        total = 1
        num_of_nums = 0
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = total + 1
        for key in dict.keys():
            if dict[key] != 2:
                return key
