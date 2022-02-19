def first_index(nums, target):
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
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        lst.append(first_index(nums, target))
        lst.append(second_index(nums, target))
        return lst
    
