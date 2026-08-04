class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS = {}
        for i in range(len(nums)):
            if target - nums[i] in hashS:
                return [hashS[target - nums[i]], i]
            else:
                hashS[nums[i]] = i
        return -1