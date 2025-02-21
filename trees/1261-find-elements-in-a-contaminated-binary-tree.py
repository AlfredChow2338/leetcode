from typing import Optional

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered = set()
        def dfs(node, value):
            if not node:
                return
            self.recovered.add(value)
            dfs(node.left, value * 2 + 1)
            dfs(node.right, value * 2 + 2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recovered