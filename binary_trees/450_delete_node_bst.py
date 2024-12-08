# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            # something right side
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # something left side
            root.left = self.deleteNode(root.left, key)
        else:
            # value is equal
            if root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            elif not root.right and not root.left:
                return None
            else:
                # both child node present:
                # find max child node from left subtree
                curr = root.left
                while curr.right:
                    curr = curr.right
                # delete that max child node from left subtree
                # since it is a leaf node no child node present
                root.val = curr.val
                root.left = self.deleteNode(root.left, curr.val)
        return root
