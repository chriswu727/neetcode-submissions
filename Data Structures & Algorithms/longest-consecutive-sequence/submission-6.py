class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        res = 0
        for n in numS:
            if n - 1 not in numS:
                length = 0
                while length + n in numS:
                    length += 1
                res = max(res, length)
        return res