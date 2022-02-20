"""Given a string s consisting of small English letters, find and return
the first instance of a non-repeating character in it. 
If there is no such character, return '_'
"""
def solution(s):
    d = {}
    arr = []
    for letter in s:
        if letter not in d:
            d[letter] = 1
            arr.append(letter)
        else:
            d[letter] += 1
    for letter in arr:
        if d[letter] == 1:
            return letter
    return "_"
