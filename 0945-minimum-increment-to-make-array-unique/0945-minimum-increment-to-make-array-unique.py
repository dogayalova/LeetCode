class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = abs(nums[i-1] - nums[i]) + 1
                nums[i] += diff
                count += diff
    
        return count 