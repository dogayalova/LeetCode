class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search approach
        left, right = 0, x
        while left <= right: 
            mid = (left + right) // 2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1
        return right
            