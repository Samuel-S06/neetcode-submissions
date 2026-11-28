class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def findTime(rate):
            time = 0
            for p in piles:
                time += math.ceil(float(p) / rate)
            return time

        l, r = 1, max(piles)
        bestTime = 0

        while l <= r:
            mid = (l + r) // 2

            midTime = findTime(mid)

            if midTime <= h:
                bestTime = mid
                r = mid - 1
            elif midTime > h:
                l = mid + 1
        
        return bestTime
            

        