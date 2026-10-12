class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Solution is to map out all connected 1's by calling dfs on each grid cell if val is 1
        # From there we recursively call DFS to set all connected(including self) cell vals
        # that are 1 to 0
        # this way we can isolate 1 counts and increment IslandCount...
        directions = [[1,0], [-1, 0], [0, 1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r>= rows or c >= cols or grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for direction in directions:
                dfs(r+direction[0], c+direction[1])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands