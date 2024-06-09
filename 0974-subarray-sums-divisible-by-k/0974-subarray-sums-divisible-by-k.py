class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            # Dictionary to store frequency of cumulative sum remainders
            # Initialize with 0:1 to handle subarrays from        index 0
        remainder_count = {0: 1}  
        cumulative_sum = 0
        result = 0

        for num in nums:
            cumulative_sum += num
            # Compute remainder of cumulative sum divided by k
            remainder = cumulative_sum % k

            # Adjust remainder to be positive (Python's modulo can return negative               # remainders)
            if remainder < 0:
                remainder += k

            # If this remainder has been seen before, add its frequency to the result
            if remainder in remainder_count:
                result += remainder_count[remainder]

            # Update the frequency of the current remainder
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return result