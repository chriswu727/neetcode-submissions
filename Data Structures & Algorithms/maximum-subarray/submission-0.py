class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            sub = max(sub, curSum)
        return sub
