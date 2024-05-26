class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        enumerated_s = dict(enumerate(s))
        enumerated_t = dict(enumerate(t))
        reversed_s = {value: key for key, value in enumerated_s.items()}
        reversed_t = {value: key for key, value in enumerated_t.items()}
        result = []
        for a in s:
            for b in t:
                if a == b:
                    result.append(abs(reversed_s[a]-reversed_t[b]))
                    
                    
        return sum(result)