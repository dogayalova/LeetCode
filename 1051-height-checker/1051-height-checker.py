class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        dif = []
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                dif.append(i)
        return len(dif)