class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        curMax = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curP = prices[r] - prices[l]
                curMax = max(curP, curMax)
            else:
                l = r
            r += 1

        return curMax 