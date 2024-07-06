class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        remaining_time = time % (2*(n-1))
        
        position = 1
        direction = 1
        
        for _ in range(remaining_time):
            if position == n:
                direction = -1
            elif position == 1:
                direction = 1
            position += direction
    
        return position