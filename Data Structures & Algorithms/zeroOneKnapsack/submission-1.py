class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        # at each point i can select one.. so basically DFS.
        # I can basically choose to select this item or skip item
        # Dictionary for i -> profit.
        # N, M = len(profit), capacity +1
        max_profits = {}

        def dfs(i, cap):
            if i == len(profit):
                return 0
            if (i, cap) in max_profits:
                return max_profits[(i, cap)]

            if cap-weight[i] >= 0:
                max_profits[(i, cap)] = max(dfs(i+1, cap), profit[i] + dfs(i+1, cap-weight[i]))
            else:
                max_profits[(i, cap)] = dfs(i+1, cap)

            return max_profits[(i,cap)]

        return dfs(0, capacity)