class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits = []
        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                profits.append(profit)
        return sum(profits)

        