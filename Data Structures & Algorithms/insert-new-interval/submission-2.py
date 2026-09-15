class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newInterval[0]:
                res.append(intervals[i])
            elif start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
                
        res.append(newInterval)

        return res