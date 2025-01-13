
from collections import deque
from typing import Optional

# DFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lv = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lv += 1
        return lv

# Stack-based DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st = [[root, 1]]
        res = 0
        while st:
            node, dep = st.pop()
            if node:
                res = max(res, dep)
                st.append([node.left, dep + 1])
                st.append([node.right, dep + 1])
        return res