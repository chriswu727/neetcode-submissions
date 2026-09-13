class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            area = 0
            if heights[l] < heights[r]:
                area = (r - l) * heights[l]
                l += 1
            else:
                area = (r - l) * heights[r]
                r -= 1
            res = max(res, area)
        return res



