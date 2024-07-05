# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # List to store the positions of critical points
        critical_points = []
        
        # Traverse the linked list
        prev = None
        curr = head
        index = 0
        
        while curr and curr.next:
            if prev and ((curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val)):
                critical_points.append(index)
            
            prev = curr
            curr = curr.next
            index += 1
        
        # If there are fewer than two critical points, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Calculate the minimum and maximum distances between critical points
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]