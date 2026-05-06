class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        curMax = 0
        while r < len(prices):
            gain = prices[r] - prices[l]
            if gain < 0:
                l = r
            else:
                curMax = max(gain, curMax)
            r += 1
        return curMax