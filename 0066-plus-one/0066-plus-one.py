class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_list = [str(digit) for digit in digits]
        num = int("".join(str_list))
        num += 1
        digits = list((int(i) for i in str(num)))
        
        return digits