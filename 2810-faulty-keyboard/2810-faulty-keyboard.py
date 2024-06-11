class Solution:
    def finalString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "i" :
                s[0:i] = s[0:i][::-1] 
                s[i] = ""
        return "".join(s)