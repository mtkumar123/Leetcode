# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        stack = [root]
        while stack:
            n = stack.pop(0)
            if val > n.val:
                if n.right:
                    stack.append(n.right)
                else:
                    n.right = TreeNode(val)
                    break
            else:
                if n.left:
                    stack.append(n.left)
                else:
                    n.left = TreeNode(val)
                    break
        return root
