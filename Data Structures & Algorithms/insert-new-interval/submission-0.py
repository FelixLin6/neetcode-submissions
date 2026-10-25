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

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        placement = None
        for i in range(len(intervals) - 1):
            if newInterval[0] >= intervals[i][0] and newInterval[0] < intervals[i+1][0]:
                intervals.insert(i + 1, newInterval)
                break

        if not placement:
            intervals.append(newInterval)

        return self.merge(intervals)
        
                