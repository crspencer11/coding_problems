def first_index(nums, target):
        """
        function that searches for the first time the target number
        appears in sorted array and returns its position.
        """
        i = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                i = mid
                high = mid - 1
            elif nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return i
    
def second_index(nums, target):
        """
        Function that searches for the second time target number
        appears in sorted array and returns its position.
        """
        i = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                i = mid
                low = mid + 1
            elif nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return i
    
class Solution(object):
    def searchRange(self, nums, target):
        """
        Combines above functions to return array containing the two
        positions, first and last, where target number appears.
        
        If it does not appear more than once, returns an array of [-1, -1].
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        lst.append(first_index(nums, target))
        lst.append(second_index(nums, target))
        return lst
    
