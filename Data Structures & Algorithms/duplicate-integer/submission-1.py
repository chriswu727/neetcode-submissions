class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = {}
        for i, n in enumerate(nums):
            if n in hset:
                return True
            hset[n] = i
        return False
