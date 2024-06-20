class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        left, right = 1, position[-1]- position[0] #we put first ball in first place and initiate at position 1
        
        def placeBalls(force):
            count = 1 # first ball in first place
            last_place = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_place >= force:
                    count += 1
                    last_place = position[i]
                    if count == m:
                        return True
            return False
        
        while left <= right: 
            mid = (left + right) // 2
            if placeBalls(mid):
                left = mid + 1
            else:
                right = mid - 1 
                
        return right
            
            
       
            