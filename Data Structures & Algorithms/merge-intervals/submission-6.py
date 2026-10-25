class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        res = []
        intervals = sorted(intervals)
        curL, curR = intervals[0][0], intervals[0][1]
        for r in range(len(intervals)):

            newL, newR = intervals[r]
            if newL <= curR:
                if newR > curR:
                    curR = newR
            else:
                res.append((curL, curR))
                curL, curR = newL, newR


        if not res or (res and (curL, curR) != res[-1]):
            res.append((curL, curR))

        return res

            