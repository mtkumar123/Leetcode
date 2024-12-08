# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
how do I find last level?
whatever remains in queue will be null...
after iterating all elements and checking their children are null
"""


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        h = 0
        while queue:
            nullFound = False
            for i in range(0, 2**h):
                if not queue:
                    break
                n = queue.pop(0)
                if nullFound:
                    if n:
                        return False
                if not n:
                    # Once we found this every value after
                    # this needs to be null
                    nullFound = True
                    continue
                queue.append(n.left)
                queue.append(n.right)
            h += 1
        return True
