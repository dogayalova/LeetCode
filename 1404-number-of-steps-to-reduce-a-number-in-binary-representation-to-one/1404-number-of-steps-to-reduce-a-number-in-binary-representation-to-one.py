class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        def binary_to_decimal(number):
            nmb = 0
            result = []
            for i in number[::-1]:
                i = int(i)
                i = (2**nmb)*i
                result.append(i)
                nmb += 1
            return sum(map(int,result))
        
        decimal = binary_to_decimal(s)
        
        while decimal>1:
            if decimal % 2 == 0:
                decimal //= 2
                count += 1
            else:
                decimal += 1
                count += 1
            
        return count
                
        
        
        