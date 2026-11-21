class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i,price in enumerate(prices):
            for j in range(i+1,len(prices)):
                maxProf = max(maxProf,prices[j] - price)
        
        return maxProf