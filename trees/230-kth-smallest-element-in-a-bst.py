
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        st = []
        cur = root
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            s.append(node.val)
            dfs(node.right)
        dfs(root)
        return s[k-1]