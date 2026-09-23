# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        allNodes = []
        # Init queue with first node
        queue = deque()
        queue.append(root)
        # While queue isnt empty(all nodes traversed)
        while queue:
            # We want to go through every level individually
            # and after that level add all those nodes to allNodes
            tempNodes = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                tempNodes.append(curr.val)
            allNodes.append(tempNodes)
        return allNodes
            
        