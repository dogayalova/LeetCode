class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        index = 0
        while index < len(nums):
            if nums.count(nums[index]) > 1:
                nums.remove(nums[index])
                count += 1
            else:
                index += 1
        return index