class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = {}
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            hset[nums[i]] = i
        return False
