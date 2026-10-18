class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob either i+2 or i+1 basically..?
        # Recursion for every path, rob the house, take i and go to i+2 or ski pand go i+1
        current_max = 0
        res = 0
        memo = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dp(i+1), nums[i] + dp(i+2))
            
            return memo[i]
            
        return dp(0)