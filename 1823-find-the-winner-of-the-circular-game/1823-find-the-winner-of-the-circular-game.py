class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]
        lost = 0
        while len(circle) > 1:
            lost = (lost + k-1) % len(circle) 
            circle.pop(lost)
            
        return circle[0]
            