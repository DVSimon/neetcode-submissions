class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # could createa recursive call
        # Backtracking. If I add each subset to a queue but pop at correct time..?
        res = []
        queue = []
        # 
        def backtrack(i):
            # Exit condition
            if i >= len(nums):
                # append 
                res.append(queue.copy())
                return
            queue.append(nums[i])
            backtrack(i+1)
            queue.pop()
            backtrack(i+1)

        backtrack(0)
        return res
