"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x: x.start)
        max_rooms = 1
        minheap = [intervals[0].end]

        for interval in intervals[1:]:
            start, end = interval.start, interval.end

            if minheap[0] <= start:
                heapq.heappop(minheap)
                heapq.heappush(minheap, end)
            else:
                heapq.heappush(minheap, end)

            max_rooms = max(max_rooms, len(minheap))
        
        return max_rooms
            
