class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # I guess we could theoretically build a list of all unique combinations then test if the combination adds up to target sum...
        res = []
        currArr = []
        #currentSum = 0
        def dfs(i, currentSum):
            if currentSum == target:
                res.append(currArr.copy())
                return
            if currentSum > target or i >= len(nums):
                return

            currArr.append(nums[i])
            # Not properly backtracking right now...

            # i -> i -> i-> i -> pop ->i+1...
            # tgt 9
            # 2, 2, 2, 2, t2r2, t5r5, r2, (22), t3t3r3....

            #case 1 rechoose i
            dfs(i, currentSum + nums[i])
            currArr.pop()

            #case 2 increment
            # It will try it self no need to add nums[i]..
            dfs(i+1, currentSum)


            #base case
            
        dfs(0, 0)
        return res