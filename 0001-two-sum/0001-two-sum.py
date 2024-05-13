class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            i = nums.index(x)
            nums2 = nums[:i] + nums[i + 1:]
            for y in nums2:
                if x + y == target and x == y:
                    return i, nums2.index(y) +1
                if x + y == target and x != y:
                    if len(nums) == 2:
                        return i, nums.index(y) +1
                    else:
                        return i, nums.index(y)
