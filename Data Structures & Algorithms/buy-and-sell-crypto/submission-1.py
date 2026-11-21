class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestDayToSell = prices[-1]
        maxProfit = 0
        for i in range(len(prices) - 1,-1,-1):
            if bestDayToSell > prices[i]:
                maxProfit = max(maxProfit,bestDayToSell - prices[i])
            bestDayToSell = max(bestDayToSell, prices[i])
        return maxProfit

        