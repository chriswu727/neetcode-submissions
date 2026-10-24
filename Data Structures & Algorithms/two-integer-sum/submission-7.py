class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in hset:
                return [hset[t], i]
            hset[nums[i]] = i
        return False
            
        
