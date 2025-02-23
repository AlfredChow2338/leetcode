
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def contruct_tree(pre_start, pre_end, post_start):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            left_root = preorder[pre_start + 1]

            num_of_left_nodes = 1
            while postorder[post_start + num_of_left_nodes - 1] != left_root:
                num_of_left_nodes += 1
            
            root = TreeNode(preorder[pre_start])

            root.left = contruct_tree(pre_start + 1, pre_start + num_of_left_nodes, post_start)
            root.right = contruct_tree(pre_start + num_of_left_nodes + 1, pre_end, post_start + num_of_left_nodes)

            return root

        return contruct_tree(0, len(preorder) - 1, 0)