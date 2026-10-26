"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        n = len(intervals)
        starts = []
        ends = []
        for x in intervals:
            starts.append(x.start)
            ends.append(x.end)
        starts, ends = sorted(starts), sorted(ends)
        i, j, count, res = 0, 0, 0, 0
        while i < n:
            s, e = starts[i], ends[j]
            if s < e:
                count += 1
                i += 1
            elif s > e:
                count -= 1
                j += 1
            else:
                i += 1; j += 1

            res = max(res, count)

        return res
            

        