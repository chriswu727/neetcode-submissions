class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashS:
                return [hashS[diff], i]
            hashS[n] = i
        return
        