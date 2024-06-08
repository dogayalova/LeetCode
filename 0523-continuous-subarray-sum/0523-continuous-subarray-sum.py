class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the remainder and the corresponding index
        remainder_dict = {0: -1}
        cumulative_sum = 0
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            remainder = cumulative_sum % k
            
            if remainder in remainder_dict:
                # Check if the length of the subarray is at least 2
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                remainder_dict[remainder] = i
        
        return False
       