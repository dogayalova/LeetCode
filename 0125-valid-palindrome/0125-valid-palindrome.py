class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_final = []
        for x in s:
            if x.isalpha() == False and x.isdigit() == False or x ==" " :
                continue
            else:
                s_final.append(x)
        s_final = "".join(s_final)
                
        return s_final==s_final[::-1]