from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do bfs
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            next_level_nodes = []
            right_most_node = None
            while queue:
                n = queue.pop(0)
                if n.left:
                    next_level_nodes.append(n.left)
                if n.right:
                    next_level_nodes.append(n.right)
                right_most_node = n
            result.append(right_most_node.val)
            queue = next_level_nodes
        return result
