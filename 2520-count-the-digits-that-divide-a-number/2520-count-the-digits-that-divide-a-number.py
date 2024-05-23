class Solution:
    def countDigits(self, num: int) -> int:
        count = []
        for a in str(num):
            if num%int(a)==0:
                count.append(a)
        return len(count)