class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for idx, interval in enumerate(intervals):
            # no overlap
            # new interval left
            # new interval right
            # new interval sub-merged
            if newInterval[1] < interval[0]:
                result.append(newInterval) 
                return result + intervals[idx:] # iterating through left, no more overlaps
            elif newInterval[0] > interval[1]:
                result.append(interval) # there might be still overlap on right intervaals
            else:
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1], interval[1])]
        result.append(newInterval)
        return result