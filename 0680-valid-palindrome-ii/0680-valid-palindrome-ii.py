class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome_range(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
           
        left,right =0, len(s)-1 # left is 0 and right is -1 from length of s.
        while left < right:
            if s[left] != s[right]:
                return palindrome_range(s, left+1, right) or palindrome_range(s, left, right-1)
            left += 1
            right -= 1
        return True