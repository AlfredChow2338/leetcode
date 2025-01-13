from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                same = isSameTree(node, subRoot)
                if same:
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return False
