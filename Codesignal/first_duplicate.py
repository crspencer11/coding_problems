def solution(a):
    d = {}
    for i in a: 
        if i in d:
            return i
        else:
            d[i] = i
    return -1
