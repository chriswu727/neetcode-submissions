class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        l, r = 0, len(heights) - 1
        cur = 0
        while l < r:
            if heights[l] > heights[r]:
                cur = heights[r] * (r - l)
                r -= 1
            else:
                cur = heights[l] * (r - l)
                l += 1
            maxa = max(maxa, cur)

        return maxa



