class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = set(edges[0])
        
        for edge in edges[1:]:
            common.intersection_update(edge)
            
        return sorted(common)[0]