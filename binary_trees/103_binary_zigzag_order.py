from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        left_flag = 1
        result = []
        queue = [root]
        while queue:
            level = []
            qlen = len(queue)
            for i in range(qlen):
                n = queue.pop(0)
                level.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(level[::left_flag])
            left_flag *= -1
        return result
