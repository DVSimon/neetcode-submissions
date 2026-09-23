# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:
                result.append(level)

        return result



        