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
        def dfs(root, curSum, targetSum):
            if not root:
                return False
            curSum += root.val

            # Base case for Leaf Nodes
            if not root.left and not root.right:
                return curSum == targetSum

            # Case for nodes with left child
            if dfs(root.left, curSum, targetSum):
                return True
            # Case for nodes with right child
            if dfs(root.right, curSum, targetSum):
                return True

            # I dont think we should ever hit this..
            return False

        return dfs(root, 0, targetSum)
            
        
        