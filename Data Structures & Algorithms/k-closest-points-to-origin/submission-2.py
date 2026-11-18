class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        li = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x ** 2 + y ** 2

            if len(maxheap) < k:
                heapq.heappush(maxheap, (-dist, [x, y]))
                continue
            
            # remember to negative the dist
            if dist < -maxheap[0][0]:
                heapq.heappop(maxheap)
                heapq.heappush(maxheap, (-dist, [x, y]))

        for dist, point in maxheap:
            li.append(point)
            
        return li