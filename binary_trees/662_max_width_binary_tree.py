from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # do bfs and give everything a number
        # for the position it is in
        queue = [(root, 1, 0)]
        prevnum, prevlevel = 1, 0
        result = 1

        while queue:
            n, num, level = queue.pop(0)

            if level > prevlevel:
                # This means this is a new level
                # and this is the first left node
                prevlevel = level
                prevnum = num

            result = max(result, num - prevnum + 1)
            if n.left:
                queue.append((n.left, 2 * num, level + 1))
            if n.right:
                queue.append((n.right, (2 * num) + 1, level + 1))
        return result
