# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we want DFS but to always return both current node height AND if the global is t/f
        def dfs(root):
            if not root:
                return [True, 0]
            #recursively DFS left and right
            left = dfs(root.left)
            right = dfs(root.right)

            #check heights AND globals
            # We need to check that left and right zeroth index are True
            # We need to check that the current l/r is balanced (+/- 1)
            # if either is false we return false and height
            # if true we return true
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            if balanced:
                # The height of a tree node is defined as the length of the longest downward path from that node to a leaf node
                # if its balanced we return T + the height of node
                # which is just the max of its left or right + 1
                return [True, 1 + max(left[1], right[1])]
            else:
                return [False, 1 + max(left[1], right[1])]

        # Run DFS and get T/f
        return dfs(root)[0]