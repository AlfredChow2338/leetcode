
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        res = []
        i, n = 0, len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            
            if depth < len(res):
                res[depth] = node
            else:
                res.append(node)
            
            if depth > 0:
                parent = res[depth - 1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node

        return res[0]