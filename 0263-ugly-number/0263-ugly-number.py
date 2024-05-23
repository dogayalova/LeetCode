class Solution:
    def isUgly(self, n: int) -> bool:
        ugly = [2,3,5]
        if n<= 0:
            return False 
    
        for a in ugly:
            while n%a == 0:
                n = n/a
        return n ==1


        