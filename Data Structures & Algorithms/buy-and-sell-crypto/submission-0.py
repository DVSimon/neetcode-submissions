class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        tempMax = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[i] < prices[j]:
                tempMax = prices[j] - prices[i]
                maxProfit = max(maxProfit, tempMax)
            else:
                i = j
        return maxProfit


        