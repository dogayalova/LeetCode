class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        s_index = 0
        
        while t_index < len (t) and s_index < len(s):
            if t[t_index] == s[s_index]:
                t_index += 1
            s_index += 1
         
        return len(t) - t_index