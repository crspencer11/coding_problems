class Solution(object):
    def findDuplicates(self, nums):
        """
        Returns the number(s) that occur at least twice in the given array, nums.
        
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for x in range(len(nums)):
            i = abs(nums[x]) - 1
            if nums[i] < 0:
                arr.append(i + 1)
            else:
                nums[i] = -nums[i]
        return arr
