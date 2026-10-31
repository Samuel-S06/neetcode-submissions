class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]

        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            profit = max(profit, prices[i] - minimum)
        
        return profit


        