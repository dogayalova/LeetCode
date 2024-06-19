class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def bouquetCounter(days):
            bouquet = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
                else:
                    flowers = 0
                
                if bouquet >= m:
                    return True
                
            return False
        
                    
        if m*k > len(bloomDay):
            return -1
        
        
        low, high = min(bloomDay), max(bloomDay)
        
        while low < high:
            mid = (low+high)//2
            if bouquetCounter(mid):
                high = mid
            else:
                low = mid + 1
                
        return low if bouquetCounter(low) else -1
        
        
        