class Solution(object):
    def firstBadVersion(self, n):
        """Finds first instance of a bad version and returns it.
        
        :type n: int
        :rtype: int
        """
        x = 0
        y = n
        while x < y:
            mid = (x + y) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    y = mid - 1
            else:
                x = mid + 1
        return y
        
