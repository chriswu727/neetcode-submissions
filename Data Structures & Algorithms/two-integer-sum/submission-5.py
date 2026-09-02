class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hset:
                return [hset[temp], i]
            hset[nums[i]] = i
        return False