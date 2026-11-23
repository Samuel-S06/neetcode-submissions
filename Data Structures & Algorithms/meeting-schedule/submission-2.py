"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):
            return True

        intervals.sort(key=lambda x: x.start)
        currEnd = intervals[0].end

        for inter in intervals[1:]:
            start = inter.start
            end = inter.end
            if start < currEnd:
                return False
            currEnd = end
        
        return True

