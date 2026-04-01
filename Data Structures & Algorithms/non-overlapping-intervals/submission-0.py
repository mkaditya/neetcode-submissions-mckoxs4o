class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval:interval[1])
        prev_end = intervals[0][1]
        res = 0

        for idx in range(1, len(intervals)):
            if prev_end > intervals[idx][0]:
                res += 1
            else:
                prev_end = intervals[idx][1]
        return res