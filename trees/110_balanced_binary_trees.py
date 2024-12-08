class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(node, balanced):
            lheight = -1
            rheight = -1
            lbalanced = True
            rbalanced = True
            if node.left:
                lbalanced, lheight = dfs(node.left, balanced)
            if not lbalanced:
                return False, None
            if node.right:
                rbalanced, rheight = dfs(node.right, balanced)
            if not rbalanced:
                return False, None
            height = max(lheight, rheight) + 1
            if abs(rheight-lheight) > 1:
                return False, None
            return balanced, height
        balanced, height = dfs(root, True)
        return balanced