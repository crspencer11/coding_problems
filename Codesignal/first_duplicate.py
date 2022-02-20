"""Given an array a that contains only numbers in the range from 1 to a.length, find the 
first duplicate number for which the second occurrence has the minimal index.
"""
def solution(a):
    d = {}
    for i in a: 
        if i in d:
            return i
        else:
            d[i] = i
    return -1
