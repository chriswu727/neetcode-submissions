class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = nums[0]
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            sub = max(sub, cur)
        return sub