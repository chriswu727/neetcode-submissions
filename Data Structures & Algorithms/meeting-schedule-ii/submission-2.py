"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        room = 0
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        s = 0
        e = 0
        while s <len(start):
            if start[s] < end[e]:
                s += 1
                room += 1
                res = max(res, room)
            else:
                e += 1
                room -= 1
        return res

