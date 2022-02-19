class Solution(object):
    """
    Returns true if any value appears at least twice in array, nums.
    Otherwise, returns false.
    """
    def containsDuplicate(self, nums):
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
