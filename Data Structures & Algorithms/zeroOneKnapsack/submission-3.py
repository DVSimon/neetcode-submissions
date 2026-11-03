class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = {}

        def dfs(i, capacity):
            # if i is out of bounds
            if i == len(profit):
                return 0
            if (i, capacity) in cache:
                return cache[(i, capacity)]
            
            # dont become burdened
            if capacity - weight[i] >= 0:
                cache[(i, capacity)] = max(profit[i] + dfs(i+1, capacity-weight[i]), dfs(i+1, capacity))
            else:
                cache[(i, capacity)] = dfs(i+1, capacity)

            return cache[(i, capacity)]

        return dfs(0, capacity)