from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_deque = deque()
        min_deque = deque()
        max_size = 0
        
        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
             
                
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()
            
            
            if min_deque and max_deque and nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
           
            max_size = max(max_size, (right - left + 1))
                
            
        return max_size