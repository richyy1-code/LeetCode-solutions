class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        totalProfit = 0
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                totalProfit += profit
        return totalProfit

        