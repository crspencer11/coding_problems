def first_index(nums, target):
        """
        Searches for first time the target value occurs in sorted array, nums.
        Returns its position in the sorted array on the left half.
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
        Searches for second time the target value shows up in sorted array, nums.
        Returns its position in the sarray on the right half.
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
        Finds starting and ending position of target in sorted array, nums.
        Returns the two positions in an array of size 2.
        
        If not found, returns [-1, -1].
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        lst.append(first_index(nums, target))
        lst.append(second_index(nums, target))
        return lst
    
