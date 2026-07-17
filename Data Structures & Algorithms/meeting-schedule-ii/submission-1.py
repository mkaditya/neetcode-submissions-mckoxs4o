class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda interval:interval.start)

        meeting_room_marker = []
        heapq.heappush(meeting_room_marker, intervals[0].end)

        for idx in range(1, len(intervals)):
            curr_meeting = intervals[idx]
            if meeting_room_marker[0] <= curr_meeting.start:
                heapq.heappop(meeting_room_marker)
            heapq.heappush(meeting_room_marker, curr_meeting.end)
        
        return len(meeting_room_marker)