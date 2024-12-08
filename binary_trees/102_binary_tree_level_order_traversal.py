# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            nodes_to_add = []
            level_result = []
            while queue:
                n = queue.pop(0)
                level_result.append(n.val)
                if n.left:
                    nodes_to_add.append(n.left)
                if n.right:
                    nodes_to_add.append(n.right)
            result.append(level_result)
            queue = nodes_to_add
        return result
