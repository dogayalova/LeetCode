class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
    
        nums.sort()
    
    # Calculate the minimum difference after at most three moves
        return min(
            nums[-1] - nums[3],  # Changing the 3 smallest elements
            nums[-2] - nums[2],  # Changing the 2 smallest elements and the largest element
            nums[-3] - nums[1],  # Changing the smallest element and the 2 largest elements
            nums[-4] - nums[0]   # Changing the 3 largest elements
        )