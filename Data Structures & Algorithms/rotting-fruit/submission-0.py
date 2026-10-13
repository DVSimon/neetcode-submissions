class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if all(value in (0,2) for row in grid for value in row):
            return 0

        if all(value in (0,1) for row in grid for value in row):
            return -1

        # Get initial rotten fruit points
        points = [
            (r,c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value == 2
        ]
        rows, cols = len(grid)-1, len(grid[0])-1
        minutes = 0
        queue = deque(points)
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        #visited = set()

        while queue:
            print("Looping")
            
            # Exit loop
            if all(value in (0,2) for row in grid for value in row):
                return minutes


            for _ in range(len(queue)):
                dr, dc = queue.popleft()
                print(f"dr:{dr}, dc:{dc}")
                for nr, nc in neighbors:
                    newRow, newCol =   dr+nr, dc+nc
                    print(f"nr:{newRow}, nc:{newCol}")
                    if(0<=newRow<=rows and 0<=newCol<=cols and grid[newRow][newCol] == 1):
                        print(f"nr:{newRow}, nc:{newCol}")
                        grid[newRow][newCol] = 2
                        queue.append((newRow,newCol))
            minutes += 1

        return -1