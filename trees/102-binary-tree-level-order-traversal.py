# Definition for a binary tree node.
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            lv = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    lv.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(lv) if lv else None
        return res