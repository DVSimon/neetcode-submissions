# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depthFirstSearch(root):
            if not root:
                # Keep node true and when leaf child the height is 0
                return [True, 0]

            # Recursively call DFS on left and right nodes
            left, right = depthFirstSearch(root.left), depthFirstSearch(root.right)
            # Get the height difference ( 2nd element )
            # At leaf children we returned 0 earlier
            heightDiff = abs(left[1] - right[1])
            # If the children nodes are balanced and the height diff of both is <= 1 we're true
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                # return true AND add 1 to the height
                return [True, 1 + max(left[1], right[1])]
            else:
                # return false AND add 1 to the height(doesnt matter)
                return [False, 1 + max(left[1], right[1])]

        # Get the value of the bool
        
        return depthFirstSearch(root)[0] 




        