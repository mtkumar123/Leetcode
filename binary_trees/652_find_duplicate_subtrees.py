# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        mapper = {}

        def dfs(node):
            if not node.left and not node.right:
                path = f"{node.val},null,null"
                if path not in mapper:
                    mapper[path] = [node]
                else:
                    mapper[path].append(node)
                return path
            path = f"{node.val}"
            if not node.left:
                path += ",null"
            else:
                path += f",{dfs(node.left)}"
            if not node.right:
                path += ",null"
            else:
                path += f",{dfs(node.right)}"
            if path not in mapper:
                mapper[path] = [node]
            else:
                mapper[path].append(node)
            return path

        dfs(root)
        result = []
        for k, v in mapper.items():
            if len(v) > 1:
                result.append(v[0])
        return result
