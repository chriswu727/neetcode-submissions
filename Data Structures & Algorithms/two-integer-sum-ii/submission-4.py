class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hs = {}
        for i in range(len(numbers)):
            re = target - numbers[i]
            if re in hs:
                return [hs[re] + 1, i + 1]
            hs[numbers[i]] = i
        return False
