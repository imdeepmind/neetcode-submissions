class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        a1, a2 = 0, 1
        max_profit = float('-inf')

        while a2 < len(prices):
            if prices[a1] < prices[a2]:
                profit = prices[a2] - prices[a1]
                max_profit = max(max_profit, profit)
            else:
                a1 = a2
            a2 += 1
        return max(0, max_profit)
