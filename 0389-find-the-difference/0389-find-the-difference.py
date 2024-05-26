class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for char in s:
            d[char] = s.count(char)
        for char in t:
            if char in d.keys() and d[char] != t.count(char):
                return char
            if char not in d.keys():
                return char
            
            
            