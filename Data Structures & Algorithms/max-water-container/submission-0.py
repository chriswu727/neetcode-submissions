class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxW = 0
        while l < r:
            width = r - l
            if heights[l] > heights[r]:
                maxW = max(maxW, width * heights[r])
                r -= 1
            else:
                maxW = max(maxW, width * heights[l])
                l += 1
        return maxW
