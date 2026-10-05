class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(sR, sC, mR, mC):
            if (sR,sC) in visited:
                return 0
            if sR < 0 or sR >= mR:
                return 0
            if sC < 0 or sC >= mC:
                return 0

            visited.add((sR, sC))

            if grid[sR][sC] == 0:
                return 0



            return (1+ 
            dfs(sR+1, sC, mR, mC) +
            dfs(sR-1, sC, mR, mC) +
            dfs(sR, sC+1, mR, mC) +
            dfs(sR, sC-1, mR, mC))

        for j in range(len(grid)):
            for i in range(len(grid[j])):
                if grid[j][i] == 1:
                    a = dfs(j, i, maxRow, maxCol)
                    maxArea = max(maxArea, a)
        return maxArea