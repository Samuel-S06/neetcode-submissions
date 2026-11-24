class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        query_pair = []
        
        for i in range(len(queries)):
            query_pair.append([i, queries[i]])
        
        query_pair.sort(key=lambda x: x[1])
 
        minheap = [] # (length, end) keyed by length
        results = [0] * len(queries)
        i = 0
        n = len(intervals)
        start, end = 0, 1

        for idx, q in query_pair:
            # push all intervals before and including q
            while i < n and intervals[i][start] <= q:
                left, right = intervals[i][start], intervals[i][end]
                length = right - left + 1
                heapq.heappush(minheap, (length, right))
                i += 1
            
            # pop all intervals that end strictly before q
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            if not minheap:
                results[idx] = -1
            else:
                results[idx] = minheap[0][0]
        
        return results
            




        