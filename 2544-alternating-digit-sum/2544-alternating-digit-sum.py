class Solution:
    def alternateDigitSum(self, n: int) -> int:
        negatives = []
        digits = str(n).strip()
        for i in range(len(digits)):
            if i % 2 == 1:
                negatives.append(int(digits[i]))
        result = sum(int(digit) for digit in digits) - (2*sum(negatives))
        return result