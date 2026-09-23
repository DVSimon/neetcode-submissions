# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMinimumNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None
        # Two cases for BST Deletion
        # Case 1: Node has 0 or 1 children, Find the node. Then replace it with other one. Also need to remove other one
        # Case 2: Two children. Find the Node to delete then find the min in it's sub tree.

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # found the node
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                # handle 2 cases
                minNode = self.findMinimumNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root

        return root



        