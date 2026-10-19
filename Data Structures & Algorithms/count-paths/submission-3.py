class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom up...
        # Previous row in 0's to the length of how many cols we have
        prevRow = [0] * n

        # Start at last row, move down 1 until 0th row done
        for r in range(m-1, -1, -1):
            # Cur row in 0's to the length of how many cols we have, reset each time
            curRow = [0] * n
            # We know the last element is 1 because can only move down
            curRow[n-1] = 1
            # Start at second last col(last is always 1)
            # Equal to row at col spot below + col to the right values
            for c in range(n-2, -1, -1):
                curRow[c] = prevRow[c] + curRow[c+1]
            # Set prev row equal to cur row after done calculating
            prevRow = curRow
        # return first value.
        return prevRow[0]

