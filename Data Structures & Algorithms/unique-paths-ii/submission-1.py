class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        # Add memoization top down
        # Brute Force
        def dfs(r, c, cache):
            if r >= row or c >= col:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == row-1 and c == col-1:
                return 1
            if cache[r][c] != 0:
                return cache[r][c]

            cache[r][c] = dfs(r+1, c, cache) + dfs(r, c+1, cache)

            return cache[r][c]


        return dfs(0,0, [[0]*col for row in range(row)])
