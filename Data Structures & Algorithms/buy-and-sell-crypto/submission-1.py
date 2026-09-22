class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for sellPrice in prices:
            profit = max(profit, sellPrice - minBuy)
            minBuy = min(minBuy, sellPrice)
        return profit
        