class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Brute Force DFS...
        # We can go down or right only, need to worry about out of bounds
        # Add memoization

        def dfs(r, c, cache):
            if r >= m or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if cache[r][c] != 0:
                return cache[r][c]

            cache[r][c] = dfs(r+1, c, cache) + dfs(r, c+1, cache)

            return cache[r][c]
        
        # return dfs(0,0, [[0] * m for col in range(n)])
        return dfs(0,0, [[0] * n for row in range(m)])