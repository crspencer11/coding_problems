class Solution(object):
    def removeElement(self, nums, val):
        """Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
        The relative order of the elements may be changed.
        
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        total = 0
        for element in nums:
            if element == val:
                pass
            else:
                nums[total] = element
                total += 1
        return total
