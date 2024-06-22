class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Replacing each even by zero and every odd by one
        nums = [1 if num % 2 != 0 else 0 for num in nums]
        
        # Dictionary to store the count of prefix sums
        prefix_counts = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            # If there's a prefix with (current_sum - k), then we've found a valid subarray
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]
            # Update the count of the current prefix sum
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
        return count
        
            
                