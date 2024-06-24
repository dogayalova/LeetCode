class Solution:
    def addBinary(self, a: str, b: str) -> str:
        numa = int(a, 2)
        numb = int(b, 2)
        
        result = numa + numb
        
        return bin(result)[2:]