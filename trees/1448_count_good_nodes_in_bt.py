# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good_nodes = []

        def dfs(node, max_v):
            if node.val >= max_v:
                good_nodes.append(node.val)
                max_v = node.val
            if node.left:
                dfs(node.left, max_v)
            if node.right:
                dfs(node.right, max_v)
        
        dfs(root, root.val)
        return len(good_nodes)