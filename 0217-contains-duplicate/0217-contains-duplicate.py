class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(num in seen or seen.add(num) for seen in [set()] for num in nums)

            