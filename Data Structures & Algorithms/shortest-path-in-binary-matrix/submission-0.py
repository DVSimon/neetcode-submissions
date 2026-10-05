class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # square so equal
        size = len(grid)
        #start/end 1
        if grid[0][0] == 1 or grid [size-1][size-1] == 1:
            return -1
        #init queue at 0,0 with length 1
        # (r,c,length)
        queue = deque([(0,0,1)])
        # We need to visit every vert, horiz, and diag neighbor...
        neighborList = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (-1, 1), (1, -1), (-1, -1)]
        visited = set((0,0))
        while queue:
            r, c, length = queue.popleft()
            if r == size - 1 and c == size - 1:
                return length

            for dr, dc in neighborList:
                nr, nc = r + dr, c + dc
                if(0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 
                and (nr, nc) not in visited):
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))


        # not found
        return -1