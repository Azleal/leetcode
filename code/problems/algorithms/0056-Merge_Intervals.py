# -*- coding: utf-8 -*-
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

    __repr__ = __str__

class Solution:
    def merge(self, intervals):
        results = []
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        c = intervals[0] if len(intervals) > 0 else None
        for e in intervals:
            if c.end < e.start:
                results.append(c)
                c = e
            else:
                c.end = max(c.end, e.end)
        if c is not None:
            results.append(c)
        return results



a=[Interval(1,3), Interval(2,5), Interval(2,4), Interval(8,10),Interval(15,18)]

r=Solution().merge(a)
print(r)