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

        # Instead of recursion/DFS we can do the same with a while loop checking each next node
        
        if not root:
            return False
        # we add the current node and its currVal after subtracting the curr node val
        path = [(root, targetSum - root.val)]

        # Loop until the tree is empty..
        while path:
            # Get the next node, stack LIFO
            node, value = path.pop()
            # base case for leaf nodes, also check if sum is 0...
            if not node.left and not node.right and value == 0:
                return True

            # Append l/r with the current value - left/rights valuie
            if node.left:
                path.append((node.left, value - node.left.val))
            if node.right:
                path.append((node.right, value - node.right.val))
        return False