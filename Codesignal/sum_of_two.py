def solution(a, b, v):
    """You have two integer arrays, a and b, and an integer target value v. 
    Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. 
    Return true if such a pair exists, otherwise return false.
    """
    s = set(a)
    for i in b:
        if v - i in s:
            return True
    return False
