class Solution(object):
    def searchInsert(self, nums, target):
        """
        Searches for a target number in sorted array and returns its index.
        If it does not exist, returns index where it would be located.
        
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
