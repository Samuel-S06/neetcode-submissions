class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        start, end = 0, 1

        # Phase 1: Append interval before intervals
        while i < n and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1
        
        # Phase 2: Append the newInterval
        while i < n and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
        res.append(newInterval)

        # Phase 3: Append the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res


