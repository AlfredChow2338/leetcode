
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        if not root:
            return True

        def dfs(cur):
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            self.diff = max(self.diff, abs(left - right))
            return 1 + max(left, right)
        
        dfs(root)
        
        return self.diff <= 1


