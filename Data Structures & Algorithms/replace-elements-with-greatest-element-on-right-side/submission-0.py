class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newmax = 0
        rightmax = -1

        for i in range(len(arr) - 1, -1, -1):
            newmax = max(rightmax, arr[i])
            arr[i] = rightmax
            rightmax = newmax
        
        return arr