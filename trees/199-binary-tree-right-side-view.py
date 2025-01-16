
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            right = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    right = node.val
                    q.append(node.left)
                    q.append(node.right)
            if right or right == 0:
                res.append(right)
        return res
