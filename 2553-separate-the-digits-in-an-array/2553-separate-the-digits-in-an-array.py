class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        no_space = "".join(str(i) for i in nums)
        return list(map(int,no_space))