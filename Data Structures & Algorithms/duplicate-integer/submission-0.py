class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashS = {}
        for i, n in enumerate(nums):
            if n in hashS:
                return True
            hashS[n] = i
        return False