class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion first

        # add caching
        memo = {}
        def fibo(n):
            if n<=2:
                return n
            if n in memo:
                return memo[n]

            n1 = fibo(n-1)
            n2 = fibo(n-2)

            memo[n] = n1+n2 

            return memo[n]

        return fibo(n)