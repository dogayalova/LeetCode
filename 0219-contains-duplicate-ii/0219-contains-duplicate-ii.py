class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Sliding Window approach
        window = set()
        
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            
            if len(window) >k:
                window.remove(nums[i - k]) 
#If the size of the window exceeds \U0001d458,remove the element that is k steps behind nums[i] from the window to maintain the window size.
                
        return False