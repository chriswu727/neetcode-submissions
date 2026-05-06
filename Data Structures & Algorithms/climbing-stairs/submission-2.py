class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1, 1
        for i in range(n-1):
            temp = dp2
            dp2 = dp1 + dp2
            dp1 = temp
        return dp2