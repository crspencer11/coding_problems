class Solution(object):
    def search(self, nums, target):
        """Splits up an array, nums, in half multiple times
        until target number is eventually found.
        
        If it is not found, returns -1.
        
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
            elif nums[mid] > target:
                high = mid - 1
            
        return -1
