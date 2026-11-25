class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_value = prices[0]
        for i in range(len(prices)):
            cur_profit = prices[i] - min_value
            if cur_profit > max_profit:
                max_profit = cur_profit
            if prices[i] < min_value:
                min_value = prices[i]
        return max_profit
        