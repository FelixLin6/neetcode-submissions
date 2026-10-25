class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        intervals = sorted(intervals)
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            L, R = intervals[i]
            if L < prevEnd:
                prevEnd = min(prevEnd, R)
                res += 1
            else:
                prevEnd = R

        return res