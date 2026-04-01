"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval:interval.start)

        for idx in range(1, len(intervals)):
            prev_interval = intervals[idx-1]
            curr_interval = intervals[idx]

            if curr_interval.start < prev_interval.end:
                return False
        return True