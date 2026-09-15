class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            lastEnd = res[-1][1]
            if lastEnd >= intervals[i][0]:
                if lastEnd < intervals[i][1]:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
            
        return res
