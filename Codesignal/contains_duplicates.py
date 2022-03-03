def solution(a):
    """Given an array of integers, write a function that determines whether the array contains any duplicates.
    Your function should return true if any element appears at least twice in the array. 
    It should return false if every element is distinct.
    """
    dict = {}
    total = 1
    if len(a) <= 1:
        return False
    for element in a:
        if element not in dict:
            dict[element] = total
        else:
            total += 1
            dict[element] = total
    if max(dict.values()) > 1:
        return True
    return False
