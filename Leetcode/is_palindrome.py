class Solution(object):
    def isPalindrome(self, x):
        """Checks whether a string is a palindrome or not.
        
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            rev = 0
            while rev < x:
                y = x % 10
                x //= 10
                rev = (rev * 10) + y
        if x == rev or x == rev // 10:
            return True
        return False
            
        
            
