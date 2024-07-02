from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        
        intersection = []
        
        for num in counts1:
            if num in counts2:
                min_count = min(counts1[num], counts2[num])
                intersection.extend([num] * min_count)
                
        return intersection