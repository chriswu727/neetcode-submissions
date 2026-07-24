class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashS:
                return [hashS[temp], i]
            hashS[nums[i]] = i
        return