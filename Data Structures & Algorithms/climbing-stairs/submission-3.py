class Solution:
    def climbStairs(self, n: int) -> int:
        # It's a binary tree, we know because 2 choices at every step.
        # So if we createa base case we can solve this.
        # Base case is when n = 1 we return 1.
        # But we also need a base case for calling on an invalid root.. (0 or 1) spot


        # Let's just go with DFS for tree...
        # n needs to be 0 or 1
        # init cache with -1's, we can't use 0 because that's a case, but should nvr be neg
        cache = [-1] * n
        def dfs(i):
            # If i is greater than n we are out of bounds, return 0
            # if i is equal to 1, we return 1(base case)
            # if i is less than(incrementing recursion) 1 we return recursive sequence
            if i > n:
                return 0
            if i == n:
                return 1
            # we can optimize by adding a cache...
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
            #return dfs(i+1) + dfs(i+2)
        return dfs(0)            
            