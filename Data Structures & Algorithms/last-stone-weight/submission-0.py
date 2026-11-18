class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) # most heaviest
            y = heapq.heappop(stones) # 2nd most 

            # y - x with pos stones --> x - y with neg stones
            # 7 - 8 = -1
            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, x - y)

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
            
        