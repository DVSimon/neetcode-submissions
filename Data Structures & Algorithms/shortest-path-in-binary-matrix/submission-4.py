class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        # No possible path if start or end are 1
        if grid[0][0] == 1 or grid[size-1][size-1] == 1:
            return -1

        # Length = 1 for starting spot
        length = 1
        # We set a queue for BFS
        # Add 0,0 point at the start
        queue = deque([(0,0)])
        # Add a visited set
        visited = {(0,0)}
        # 8 Directions
        neighborList = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (-1, 1), (1, -1), (-1, -1)]

        while queue:
            for i in range(len(queue)):
                dc,dr = queue.popleft()
                if dc == size-1 and dr == size - 1:
                        return length
                for nc, nr in neighborList:
                    newCol, newRow = dc + nc, dr + nr
                    if (0 <= newCol < size and 0 <= newRow < size and (newCol, newRow) not in visited and grid[newCol][newRow] == 0):
                        queue.append((newCol, newRow))
                        visited.add((newCol, newRow))
            length += 1
        return -1

        