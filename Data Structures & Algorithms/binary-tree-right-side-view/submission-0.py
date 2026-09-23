# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # What my assumption here is we only want to add the right most nodes of each level
        result = []

        queue = deque()
        queue.append(root)

        while(queue):
            #At each level insert the last element of queue
            lastEle = queue[-1]
            # What if the last element is null.. But we don't want to add null
            if lastEle:
                result.append(lastEle.val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
        return result
        