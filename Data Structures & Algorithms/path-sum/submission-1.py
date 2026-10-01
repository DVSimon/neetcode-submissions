# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Few thoughts - I can do this with DFS itself I think
        # For backtracking - maybe I can use a stack...
        # Try DFS first

        # Dont even need to pass targetSum in here

        def dfs(node, currentSum):
            if not node:
                return False

            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum

            return dfs(node.right, currentSum) or dfs(node.left, currentSum)

        return dfs(root, 0)