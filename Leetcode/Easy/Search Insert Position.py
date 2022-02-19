class Solution(object):
    def searchInsert(self, nums, target):
        """
        Returns index of target number in a sorted array, if it exists.
        If it doesn't, returns the index where it would be in the array
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1
