class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        total_flips = 0
        diff = [0] * (n+1)
        
        for i in range(n):
            flip_count += diff[i]
            
            if (nums[i] + flip_count) % 2 == 0: #If a bit is flipped an odd number of times, its value changes from its original state and vice versa.
                if i + k > n: # ensure that i + k - 1 is within the bounds of the array.
                    return -1
    
                flip_count += 1
                total_flips += 1
                diff[i] += 1
                if i + k < n:
                    diff[i+k] -= 1
                
        
        return total_flips
                